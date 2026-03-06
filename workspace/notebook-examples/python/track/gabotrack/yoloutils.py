
import cv2
from PIL import Image
import os


class YOLOutils:   
    """Utilidades para trabajar con modelos YOLO y detección de objetos.
    Incluye funciones para detectar objetos, dibujar bounding boxes, y manejar imágenes y videos.
    """
    __labelDetectionColor__ = (0, 0, 0)
    __labelCartesianColor__ = (0, 0, 0)  # Color para las coordenadas del plano cartesiano

    __CUSTOM_QR__     = 'gabo-qr.pt'  # Modelo personalizado para detección de QR
    __CUSTOM_FRUITS__ = 'gabo-fruits.pt'  # Modelo personalizado para detección de frutas

    __YOLOV11n__ = 'yolo11n' # Muy pequeño y rápido, pero menos preciso. Ideal para dispositivos con pocos recursos.
    __YOLOV11s__ = 'yolo11s' # Más preciso que 8n, sigue siendo rápido y ligero.
    __YOLOV11m__ = 'yolo11m.pt' # Equilibrio entre velocidad y precisión.
    __YOLOV11m_pose__ ='YOLO11m-pose.pt'
    __YOLOV11m_seg__ = 'yolo11m-seg.pt' 
    __YOLOV11l__ = 'yolo11l' # Más preciso, pero más lento y pesado.


    @staticmethod
    def getClassID(modelName, class_name = None):
        class_names = modelName.names  # Obtiene los nombres de las clases del modelo
    
        if class_name is not None:
            class_id = None
            for idx, name in class_names.items():
                if name == class_name:
                    class_id = idx
                    break
            if class_id is None:
                raise ValueError(f"Clase '{class_name}' no encontrada en el modelo.")
            classes = [class_id]
        else:
            classes = None  # Analiza todas las clases    

        return classes
    
    @staticmethod
    def detectObjects(frame, modelName, className=None, conf=0.5):  
                     
        classID = YOLOutils.getClassID(modelName, className)  # Obtiene los nombres de las clases del modelo
        results = modelName.track(frame, 
                                    persist=True, 
                                    verbose=False, 
                                    classes=classID, 
                                    show=False,
                                    conf=conf,
                                    tracker='bytetrack.yaml')  #  'botsort' , 'bytetrack'
        boxes = results[0].boxes 

        return (boxes, results)
    
    @staticmethod
    def detectQRObjects(frame, modelName,conf=0.5):  
                     
        results = modelName.track(frame, 
                                    persist=True, 
                                    verbose=False, 
                                    classes=0, 
                                    show=False,
                                    conf=conf,
                                    tracker='bytetrack.yaml')  #  'botsort' , 'bytetrack'
        boxes = results[0].boxes 

        return (boxes, results)
    
    # Realiza detección de objetos utilizando un modelo especifico
    # y retorna los bounding boxes detectados
    @staticmethod
    def drawBoundingBox(frame, boxes, qrPlane):
        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                track_id = int(box.id[0]) if box.id is not None else -1

                # Centroide del bounding box.
                # Estas coordenadas son con respecto al origen del frame actual
                # que esta en la esquina superior izquierda
                cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

                # Dibuja el bounding box y el label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                label = f'origen imagen: ({cx},{cy})'                  
                cv2.putText(frame, label, (x2 + 10, y2 - 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, YOLOutils.__labelDetectionColor__, 2)

                if qrPlane.getValidity() == True:
                    # Proyecta el centroide del bounding box al plano cartesiano
                    # utilizando la matriz de homografía calculada previamente
                    ptoCartesiano = qrPlane.projectPoint((cx, cy))
                    label = f'({ptoCartesiano[0]:.2f},{ptoCartesiano[1]:.2f})'
                    cv2.putText(frame, label, (x2 + 10, y2), cv2.FONT_HERSHEY_SIMPLEX, 1.2, YOLOutils.__labelCartesianColor__, 2)

    @staticmethod
    def drawPose(frame, results):
        frame[:] = results[0].plot(line_width=1, 
                                    conf=False, 
                                    boxes=False)
        '''
        skeletonConnections = [
            (0, 1), (1, 2), (2, 0), 
            #(3, 4), (4, 6), (3, 5), 
            #(5, 6), 
            (6, 8), (8, 10), 
            (5, 7), (7, 9), 
            #(6, 12), (11,12), (5,11),
            #(12, 14), (14, 16),
            #(11, 13), (13, 15)
        ]
        if results[0].keypoints is not None:
            # Acceder a los landmarks de la persona detectada
            #for x, y, conf in results[0].keypoints.data[0]:
            #    if conf > 0.5:
            #        cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 0), -1)
            for keys in results[0].keypoints:
                points = []
                for x,y,conf in keys.data[0]:
                    if conf > 0.5:
                        points.append((int(x), int(y))) 
                        cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 0), -1)
                
                # Dibujar las conexiones del esqueleto
                for (start_idx, end_idx) in skeletonConnections:
                    if start_idx < len(points) and end_idx < len(points):
                        start_point = points[start_idx]
                        end_point = points[end_idx]
                        cv2.line(frame, start_point, end_point, (0, 255, 255), 2)  # Color del esqueleto
        '''

    @staticmethod
     # Realiza un preprocesamiento del frame
    def preprocessFrame(frame, flipHorizontal = False, rotate90Clockwise = False ):
        # Nota: la imagen que está en la variable 'frame' es una referencia a la imagen original.
        # Si se modifica con frame[:] = ..., se modifica el frame original

        # Aplica efecto espejo horizontal
        if flipHorizontal:
            frame[:] = cv2.flip(frame, 1)  
        
        # Rotar 90 grados
        if rotate90Clockwise == True:
            frame[:] = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                

    @staticmethod
    def isImageFile(filename):
        """
        Verifica si un archivo es una imagen basándose en su encabezado y extensión.

        Args:
            ruta_archivo: La ruta al archivo que se va a verificar.

        Returns:
            Una tupla (es_imagen, formato, dimensiones) donde:
            - es_imagen:  True si el archivo es una imagen reconocida, False en caso contrario.
            - formato: El formato de la imagen (e.g., "JPEG", "PNG"), o None si no es una imagen.
            - dimensiones: Una tupla (ancho, alto) de la imagen, o None si no es una imagen.
        """
        if os.path.exists(filename):
            try:
                with Image.open(filename) as img:
                    format = img.format
                    dims = img.size
                    return True, format, dims
            except IOError:  # Pillow lanza IOError si no puede identificar el archivo como una imagen
                return False, None, None
            