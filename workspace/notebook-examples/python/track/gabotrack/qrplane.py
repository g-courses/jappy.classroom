from ultralytics import YOLO
import numpy as np
import cv2
from .homography import Homography
from .yoloutils import YOLOutils
#from .cartesianplane import CartesianPlane

    
class QRPlane:
    # Dimensiones del plano cartesiano
    # Estas dimensiones son fijas durante el analisis y se utilizan para proyectar puntos 
    # del plano proyectivo al plano cartesiano
    # y viceversa. Se asume que el origen del plano cartesiano está en la esquina superior izquierda
    # y que las coordenadas aumentan hacia la derecha y hacia abajo.
    # Las dimensiones se definen en centímetros para facilitar la proyección de puntos
    # y la visualización en un plano cartesiano.
    __cartesian_width__    = 84.5
    __cartesian_length__   = 162

    def __init__(self):
        self.matrixHomography = None
        self.frame = None

        self.validity = False  # Indica si el plano QR es válido (se detectaron 4 QR)

        # Diccionario para almacenar las coordenadas de los QR detectados
        # Estas coordenadas se utilizan para calcular la homografía
        # y proyectar puntos del plano proyectivo al plano cartesiano
        self.qrFrameCoord = {}  

    def determineQRPlane(self, 
                         frame, 
                         detectQR_conf, 
                         cartesian_in_centroid_qr, 
                         showQRBoundingBoxes,
                         showQRProyectivePlane,
                         showPlaneVertices):
        
        self.setFrame(frame)
        # Realiza la detección de los códigos QR utilizando el modelo específico
        # y luego realiza el análisis de los QR detectados.            
        if self.getValidity() == False:
            self.detectQR(conf=detectQR_conf)  # Detecta los códigos QR en el frame actual
            if self.getValidity() == True:
                self.calcQRCoord(centroid=cartesian_in_centroid_qr,
                                         showQRBoundingBoxes=showQRBoundingBoxes )
                
                self.calcMatrixHomography()
                self.matrixHomography = self.getMatrixHomography()
                print("Matriz de homografía:\n",self.matrixHomography)

        if self.getValidity() == True and showQRProyectivePlane == True:
            self.showProyectivePlane()
            

        if self.getValidity() == True and showPlaneVertices == True:
            #self.showCoords()
            self.showVertices()

    def setFrame(self, frame):
        # Establece un nuevo frame y recalcula las coordenadas de los QR
        self.frame = frame

    def detectQR(self, conf=0.8):
        # Detecta los códigos QR en el frame actual utilizando el modelo personalizado
        self.boxes, results = YOLOutils.detectObjects(frame=self.frame, 
                                             modelName=YOLO(YOLOutils.__CUSTOM_QR__),
                                             className='qr_code',
                                             conf=conf)

        if self.boxes is None or len(self.boxes) < 4:
            print("****AVISO******: Se detectaron " + str(len(self.boxes)) + " códigos QR. " + f"{conf=}")
            self.validity = False
        else:
            self.validity = True

    def getValidity(self):
        """
        Retorna la validez del plano QR.
        Si se detectaron exactamente 4 códigos QR, retorna True.
        De lo contrario, retorna False.
        """
        return self.validity

    def calcQRCoord(self, centroid = False, showQRBoundingBoxes = True):        
        # Los QR se ordenan por coordenada y, de arriba a abajo
        # y luego por coordenada x, de izquierda a derecha.
        # Esto asegura que los códigos QR se procesen en el orden correcto
        # para la proyección de puntos y la homografía.

        print("****QRBoxes ordenados con etiquetas******")
        for b in self.boxes:
            x1, y1, x2, y2 = map(int, b.xyxy[0])
            coords = x1, y1, x2, y2
            conf = float(b.conf[0])
            print(conf, coords, b.xyxy[0][0], b.xyxy[0][1])
        

        # Ordena los bounding boxes por coordenada y
        self.boxes = sorted(self.boxes, key=lambda b: (b.xyxy[0][1], b.xyxy[0][0]))
        self.boxes = sorted(self.boxes, key=lambda b: (b.xyxy[0][0], b.xyxy[0][1]))
        
        # FALTA: asegurar que si hay mas de cuatro, seleccionar los 4 con
        #        mal alta confianza
        #
        
        # Los bounding boxes se ordenan por coordenada y, de arriba a abajo
        # se crea un diccionario con las etiquetas de los bounding boxes
        labelsBox = ['bottom-left', 'top-left', 'top-right', 'bottom-right']
        sortedBoxes = {label: self.boxes[i] for label, i in zip(labelsBox, range(len(labelsBox)))}

        print("****QRBoxes ordenados con etiquetas******")
        for label, box in sortedBoxes.items():
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            coords = x1, y1, x2, y2
            conf = float(box.conf[0])
            print(label, conf, coords)

            # Guarda las coordenadas de los bounding boxes en el diccionario qrFrameCoord
            if centroid:
                self.qrFrameCoord[label] = self.centroid(x1, y1, x2, y2)
            else:   
                # Si no se quiere el centroide, se guardan las esquinas
                if 'bottom-left' in label:
                    self.qrFrameCoord[label] = (x1, y2)  # (x1, y2) es la esquina inferior izquierda
                elif 'top-left' in label:
                    self.qrFrameCoord[label] = (x1, y1)  # (x1, y1) es la esquina superior izquierda
                elif 'top-right' in label:
                    self.qrFrameCoord[label] = (x2, y1)  # (x2, y1) es la esquina superior derecha
                elif 'bottom-right' in label:
                    self.qrFrameCoord[label] = (x2, y2)  # (x2, y2) es la esquina inferior derecha

            if showQRBoundingBoxes:
                cv2.rectangle(self.frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(self.frame, f"{label}:({x1},{y1}), ({x2},{y2})", (x2 + 10, y2+10), cv2.FONT_HERSHEY_SIMPLEX, .8, (255,255,255), 2)

    def centroid(self,x1, y1, x2, y2):
        # Centroide del bounding box
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        return cx, cy

    def showCoords(self): 
        # Muestra las coordenadas de los vertices de los códigos QR
        for key, (x, y) in self.qrFrameCoord.items():
            cv2.putText(self.frame, f'({x}, {y})', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    def calcMatrixHomography(self):
        H = Homography(points_source=np.array([self.qrFrameCoord['top-left'],
                                               self.qrFrameCoord['top-right'],
                                               self.qrFrameCoord['bottom-right'],
                                               self.qrFrameCoord['bottom-left']]),
                        points_target=np.array([(0, 0), 
                                                (self.__cartesian_width__, 0), 
                                                (self.__cartesian_width__, self.__cartesian_length__), 
                                                (0, self.__cartesian_length__)]))
        
        self.matrixHomography = H.find_homography()
    
    def getMatrixHomography(self):
        if self.matrixHomography is None:
            raise ValueError("La matriz de homografía no ha sido calculada. Llama a getHomography() primero.")
        return self.matrixHomography
    
    def showVertices(self):
        if self.getValidity() == True:
            for (x,y) in self.qrFrameCoord.values():
                cv2.circle(self.frame, (x, y), 10, (0, 255, 255), -1)
                ptoCartesiano = self.projectPoint((x, y)) ############
                cv2.putText(self.frame, f'({ptoCartesiano[0]:.2f}, {ptoCartesiano[1]:.2f})', (x, y + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, YOLOutils.__labelCartesianColor__, 2)    


    def showProyectivePlane(self):
        # Dibuja las líneas que unen los vertices de los códigos QR
        colorLineas = (255, 0, 255)
        grosorLineas = 3
        cv2.line(self.frame, self.qrFrameCoord['top-right']   , self.qrFrameCoord['bottom-right'], colorLineas, grosorLineas)
        cv2.line(self.frame, self.qrFrameCoord['top-left']    , self.qrFrameCoord['bottom-left'] , colorLineas, grosorLineas)
        cv2.line(self.frame, self.qrFrameCoord['top-right']   , self.qrFrameCoord['top-left']    , colorLineas, grosorLineas)
        cv2.line(self.frame, self.qrFrameCoord['bottom-right'], self.qrFrameCoord['bottom-left'] , colorLineas, grosorLineas)

    # Proyecta un punto del plano proyectivo al plano cartesiano
    # Utiliza la matriz de homografía para realizar la transformación
    # El punto debe estar en formato (x, y) en el plano proyectivo
    # Retorna el punto proyectado en el plano cartesiano como (x, y)
    # El punto proyectivo debe estar en formato (x, y) y se asume que z=1
    # para simplificar la proyección.
    # La matriz de homografía debe ser previamente calculada y asignada a self.matrixHomography
    def projectPoint(self, pointProjectivo):
        # Convertir el punto al formato proyectivo
        P_proj = np.array([pointProjectivo[0], pointProjectivo[1], 1])
        
        # Aplicar la matriz self.H
        Q_proj = self.matrixHomography @ P_proj
        
        # Normalizar para obtener el punto en el plano cartesiano
        Q_cartesian = Q_proj[:2] / Q_proj[2]
        
        return Q_cartesian
