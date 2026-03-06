from ultralytics import YOLO
import cv2
import re
import numpy as np
from IPython.display import Image, display, clear_output

from .yoloutils import YOLOutils
from .qrplane   import QRPlane


class Analysis:
    """!
    @brief [Description de la classe]

    """

    __labelDetectionColor__ = (0, 0, 0)
    __labelCartesianColor__ = (255, 255, 255) 
    __backgroundGrayColor__ = 128 

    __flipHorizontal__     = False
    __rotate90Clockwise__    = False  # Si True, rota el frame 90 grados en sentido horario

    __appName__            = 'YOLOv8 Tracking ErrGAboV0'

    __determineQRPlane__   = False
    __detectQR_conf__      = 0.8
    __showQRProyectivePlane__ = False
    __showQRBoundingBoxes__ = False

    __detectPerson_conf__  = 0.5

    __cartesian_width__    = 84.5
    __cartesian_length__   = 162
    __cartesian_in_centroid_qr__ = False

    __showCartesian__      = False
    __showPlaneVertices__  = False

    __videoOutWrite__      = False
    __showBoundingBoxes__  = False
    __showBoxLabel__       = False
    __trackEnabled__       = True  # Si True, dibuja las trayectorias de los objetos detectados
    __trackLineColor__     = (255, 128, 0)  # Color de la línea de la trayectoria 
    __trackAlwaysVisible__ = True  # Si True, las trayectorias se dibujan aunque el track_id ya no esté en el frame
    __videoTrajectories__  = True  # Si True, guarda las trayectorias en un video separado
    __imgTrajectories__    = True  # Si True, guarda las trayectorias en una imagen

    __saveImageDetection__ = True  # Si True, guarda la imagen con las detecciones

    
    def __init__(self, videoInPath, modelNames, idCamera=None, class_name=None):
        """!
        @brief [Constructor de la clase Analysis]

        Parameters : 
            @param videoInPath => [Ruta del video o imagen de entrada]
            @param modelNames => [Lista de modelos YOLO a utilizar para la detección]
            @param idCamera = None => [Identificador de la cámara (opcional, si se quiere usar una cámara en lugar de un video)]
            @param class_name = None => [Clase a detectar (opcional, si se quiere filtrar por una clase específica)]

        """

        self.qrPlane = None
        self.matrixHomography = None


        # Diccionario para almacenar trayectorias por track_id
        self.tracks = {}  
        self.tracksCartesian = {}  


        # A partir del parametro modelNames, se crea un diccionario de modelos,
        # cuya clave es el nombre del modelo y su valor es una instancia de YOLO.
        self.models = {name: YOLO(name) for name in modelNames}


        self.class_name = class_name  # Nombre de la clase a detectar (opcional)
        self.isImage = False

        if idCamera is not None:
            # Si se proporciona un ID de cámara, usa la cámara en lugar de un archivo de video
            self.videoInPath = idCamera
            self.videoIn = cv2.VideoCapture(self.videoInPath)

            self.videoOutPath          = None
            self.videoTrajectoriesPath = None
            self.imgTrajectoriesPath   = None
            self.videoOut              = None

            self.__videoOutWrite__     = False  # Por defecto no guarda el video de salida
            self.__videoTrajectories__ = False
            self.__imgTrajectories__   = False
        else:
            # Si no se proporciona un ID de cámara, usa el archivo de video o una imagen
            self.isImage, format, dims = YOLOutils.isImageFile(videoInPath)
            if self.isImage:
                self.imgInPath = videoInPath
                self.imgIn = cv2.imread(self.imgInPath)
                self.imgOutPath = re.sub(r'([^/]+)(?=\.[^.]+$)', r'\1_detected', self.imgInPath)

            else:
                self.videoInPath = videoInPath
                self.videoIn = cv2.VideoCapture(self.videoInPath)

                self.videoOutPath          = re.sub(r'([^/]+)(?=\.[^.]+$)', r'\1_track', self.videoInPath)
                self.videoTrajectoriesPath = re.sub(r'([^/]+)(?=\.[^.]+$)', r'\1_trajec', self.videoInPath)
                self.imgTrajectoriesPath   = re.sub(r'\..*$', '.png', self.videoInPath)

                self.imgCartesianTrajectoriesPath = re.sub(r'([^/]+)(?=\.[^.]+$)', r'\1_cartesian', self.imgTrajectoriesPath)

                

    def saveTrajectoriesVideo(self):
        # Obtiene propiedades del video original
        width  = int(self.videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps    = self.videoIn.get(cv2.CAP_PROP_FPS)

        # Crea el objeto VideoWriter para el video de trayectorias
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        traj_out = cv2.VideoWriter(self.videoTrajectoriesPath, fourcc, fps, (width, height))

        max_len = max(len(pts) for pts in self.tracks.values())
        for frame_idx in range(max_len):
            traj_frame = np.ones((height, width, 3), dtype=np.uint8) * self.__backgroundGrayColor__
            for pts in self.tracks.values():
                # Solo dibuja hasta el punto actual
                visible_pts = pts[:frame_idx+1]
                for i in range(1, len(visible_pts)):
                    pt1 = tuple(map(int, visible_pts[i - 1]))
                    pt2 = tuple(map(int, visible_pts[i]))
                    cv2.line(traj_frame, pt1, pt2, self.__trackLineColor__, 2)
                if len(visible_pts) > 0:
                    cv2.circle(traj_frame, tuple(map(int, visible_pts[0])), 7, (0, 255, 0), -1)
                    cv2.circle(traj_frame, tuple(map(int, visible_pts[-1])), 7, (0, 0, 255), -1)
            traj_out.write(traj_frame)
        traj_out.release()

    def saveTrajectoriesImage(self):
        width  = int(self.videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Crea una imagen con un fondo gris
        img = np.ones((height, width, 3), dtype=np.uint8) * self.__backgroundGrayColor__

        for pts in self.tracks.values():
            for i in range(1, len(pts)):
                pt1 = tuple(map(int, pts[i - 1]))
                pt2 = tuple(map(int, pts[i]))
                cv2.line(img, pt1, pt2, self.__trackLineColor__, 2)
            if len(pts) > 0:
                cv2.circle(img, tuple(map(int, pts[0])), 7, (0, 255, 0), -1)   # Punto verde inicio
                cv2.circle(img, tuple(map(int, pts[-1])), 7, (0, 0, 255), -1)  # Punto rojo final

        cv2.imwrite(self.imgTrajectoriesPath, img)


    def saveCartesianTrajectoriesImage(self):
        def sumarTuplas(tupla1, tupla2):
            if len(tupla1) != len(tupla2):
                raise ValueError("Las tuplas deben tener la misma longitud.")
            
            return tuple(a + b for a, b in zip(tupla1, tupla2))

        cartesianWidth  = int(self.__cartesian_width__)
        cartesianHeight = int(self.__cartesian_length__)

        offsetWidth  = int(.2 * cartesianWidth)
        offsetHeight = int(.2 * cartesianHeight)

        width = cartesianWidth + 2 * offsetWidth
        height = cartesianHeight + 2 * offsetHeight

        # Crea una imagen con un fondo gris
        img = np.ones((height, width, 3), dtype=np.uint8) * self.__backgroundGrayColor__

        for pts in self.tracksCartesian.values():
            for i in range(1, len(pts)):
                pt1 = tuple(map(int, pts[i - 1]))
                pt2 = tuple(map(int, pts[i]))

                pt1 = sumarTuplas(pt1, (offsetWidth, offsetHeight))
                pt2 = sumarTuplas(pt2, (offsetWidth, offsetHeight))

                cv2.line(img, pt1, pt2, self.__trackLineColor__, 2)
            if len(pts) > 0:
                cv2.circle(img, tuple(map(int, pts[0])), 7, (0, 255, 0), -1)   # Punto verde inicio
                cv2.circle(img, tuple(map(int, pts[-1])), 7, (0, 0, 255), -1)  # Punto rojo final

        cv2.imwrite(self.imgCartesianTrajectoriesPath, img)


    def begin(self):
        self.qrPlane = QRPlane()
        self.qrPlane.__cartesian_width__    = self.__cartesian_width__
        self.qrPlane.__cartesian_length__   = self.__cartesian_length__

        try:
            if self.isImage:
                self.imageAnalysis()
            else:
                self.videoAnalysis()
        except KeyboardInterrupt:
            print("Terminando programa...")


    def imageAnalysis(self):
        # Realiza un preprocesamiento del frame
        YOLOutils.preprocessFrame(frame=self.imgIn, 
                                    flipHorizontal    = self.__flipHorizontal__, 
                                    rotate90Clockwise = self.__rotate90Clockwise__)
        
        # Realiza la detección de los códigos QR utilizando el modelo específico
        # y luego realiza el análisis de los QR detectados.
        if self.__determineQRPlane__:
            #self.determineQRPlane(frame=self.imgIn)
            self.qrPlane.determineQRPlane(frame=self.imgIn,
                                          detectQR_conf=self.__detectQR_conf__,
                                          cartesian_in_centroid_qr=self.__cartesian_in_centroid_qr__,
                                          showQRBoundingBoxes=self.__showQRBoundingBoxes__,
                                          showPlaneVertices=self.__showPlaneVertices__,
                                          showQRProyectivePlane=self.__showQRProyectivePlane__)
 
        # Por cada modelo en la lista de modelos
        # Detecta objetos en el frame utilizando cada uno
        for (model, mName) in self.models.items():
            #print(f"Analizando imagen con el modelo: {model}")
            boxes, results = YOLOutils.detectObjects(frame=self.imgIn, 
                                                     conf=self.__detectPerson_conf__,
                                                     modelName=mName, className=self.class_name)  
            
            # Seguir con el resto de las clases
            # Dibujar rectangulos en el frame donde se detectaron objetos
            self.showDetection(frame=self.imgIn, boxes=boxes, 
                               modelName=mName, 
                               showBoundingBoxes=self.__showBoundingBoxes__,
                               showBoxLabel=self.__showBoxLabel__)



    def videoAnalysis(self):
        if self.__videoOutWrite__ == True:
            # Obtiene propiedades del video original
            width  = int(self.videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps    = self.videoIn.get(cv2.CAP_PROP_FPS)
            #print(f"{fps=}")

            #Define el codec y crea el objeto VideoWriter
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.videoOut = cv2.VideoWriter(self.videoOutPath, fourcc, fps, (width, height))

        while self.videoIn.isOpened():
            ret, frame = self.videoIn.read()
            if not ret:
                break

            # Realiza un preprocesamiento del frame
            YOLOutils.preprocessFrame(frame, 
                                      flipHorizontal    = self.__flipHorizontal__, 
                                      rotate90Clockwise = self.__rotate90Clockwise__)

            if self.__determineQRPlane__:
                #self.determineQRPlane(frame=frame)
                self.qrPlane.determineQRPlane(frame=frame,
                                              detectQR_conf=self.__detectQR_conf__,
                                              cartesian_in_centroid_qr=self.__cartesian_in_centroid_qr__,
                                              showQRBoundingBoxes=self.__showQRBoundingBoxes__,
                                              showPlaneVertices=self.__showPlaneVertices__,
                                              showQRProyectivePlane=self.__showQRProyectivePlane__)
            
            # Por cada modelo en la lista de modelos
            # Detecta objetos en el frame utilizando cada uno
            for (model, mName) in self.models.items():
                boxes, results = YOLOutils.detectObjects(frame, 
                                                         modelName=mName, 
                                                         className=self.class_name, 
                                                         conf=self.__detectPerson_conf__)  

                YOLOutils.drawPose(frame, results)
                
                # Seguir con el resto de las clases
                # Dibujar rectangulos en el frame donde se detectaron objetos
                self.showDetection(frame, boxes, 
                                   modelName=mName, 
                                   showBoundingBoxes=self.__showBoundingBoxes__, 
                                   showBoxLabel=self.__showBoxLabel__)

                # Dibujar TODAS las trayectorias almacenadas, aunque el track_id ya no esté en el frame
                self.drawAllTrajectories(frame)

            # Muestra el frame procesado
            if self.__videoOutWrite__ == True:
                self.videoOut.write(frame)
            cv2.imshow(self.__appName__, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                raise KeyboardInterrupt

    def showDetection(self, frame, boxes, modelName, showBoundingBoxes=True, showBoxLabel=True):
        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                track_id = int(box.id[0]) if box.id is not None else -1

                # Centroide del bounding box
                #cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
                # Centroide de la base del bounding box
                cx, cy = int( (x1 + x2) / 2), int( (y2))

                # Guarda el centroide en la trayectoria de ese track_id
                if track_id not in self.tracks:
                    self.tracks[track_id] = []
                self.tracks[track_id].append((cx, cy))

                # Dibuja el bounding box y el label
                if showBoundingBoxes:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                         
                    if showBoxLabel:
                        class_id = int(box.cls[0])  # Índice de la clase detectada
                        class_name = modelName.names[class_id]  # Nombre de la clase
                        #label = f'{class_name} {100*conf:.2f}%'
                        #label = f'ID:{track_id} {conf:.2f}'
                        label = f'{class_name}'
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, self.__labelDetectionColor__, 2)
            
                if self.qrPlane.getValidity() == True:
                    ptoCartesiano = self.qrPlane.projectPoint((cx, cy))
                    if track_id not in self.tracksCartesian:
                        self.tracksCartesian[track_id] = []
                    self.tracksCartesian[track_id].append((int(ptoCartesiano[0]), int(ptoCartesiano[1])))

                    if self.__showCartesian__:
                        ptoCartesiano = list(map(int, self.qrPlane.projectPoint((cx, cy))))
                        label = f'x={ptoCartesiano[0]:.2f} y={ptoCartesiano[1]:.2f})'
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.__labelDetectionColor__, 1)

                if not self.isImage:
                    # Dibuja la trayectoria solo si el track_id está en el frame actual
                    self.drawTrajectories(frame, track_id)
                    

    # Dibujar TODAS las trayectorias almacenadas, 
    # aunque el track_id ya no esté en el frame
    def drawAllTrajectories(self, frame):
        if self.__trackEnabled__ == True and self.__trackAlwaysVisible__ == True:
                # Dibuja TODAS las trayectorias almacenadas, aunque el track_id ya no esté en el frame
                for pts in self.tracks.values():
                    for i in range(1, len(pts)):
                        cv2.line(frame, pts[i - 1], pts[i], self.__trackLineColor__, 2)
                    
                    if len(pts) > 0:
                        # Punto verde al inicio
                        cv2.circle(frame, pts[0], 7, (0, 255, 0), -1)
                        # Punto rojo al final
                        cv2.circle(frame, pts[-1], 7, (0, 0, 255), -1)

    def drawTrajectories(self, frame, track_id):
        if self.__trackEnabled__ == True and self.__trackAlwaysVisible__ == False:                    
                        pts = self.tracks[track_id]
                        for i in range(1, len(pts)):
                            cv2.line(frame, pts[i - 1], pts[i], self.__trackLineColor__, 2)

    def end(self):
        if self.isImage:
            # Guarda la imagen de salida
            if self.__saveImageDetection__:
                cv2.imwrite(self.imgOutPath, self.imgIn)
                display(Image(filename=self.imgInPath))
                display(Image(filename=self.imgOutPath))
        else:
            if self.__videoOutWrite__ == True:
                self.videoOut.release()

            if self.__videoTrajectories__ == True:
                self.saveTrajectoriesVideo()

            if self.__imgTrajectories__ == True:
                self.saveTrajectoriesImage()

                if self.qrPlane.getValidity() == True:
                    self.saveCartesianTrajectoriesImage()


            self.videoIn.release()
            cv2.destroyAllWindows()
