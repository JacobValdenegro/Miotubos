# Myotube Detection and Segmentation Model

Este repositorio contiene los scripts necesarios para entrenar y usar un modelo de detección basado en YOLOv11, diseñado para detectar y contar myotubos en imágenes microscópicas.

## Instrucciones

1. Organiza tus datos:  
   Coloca las imágenes originales etiquetadas y sus archivos JSON correspondientes en la carpeta `Labelme`.

2. Genera imágenes espejadas horizontalmente:  
   Ejecuta el script `mirrorH.py` para generar versiones espejadas horizontalmente de las imágenes y los archivos JSON:  
   python mirrorH.py  
   Esto creará una carpeta llamada `mirrorH` con las imágenes y JSON modificados.

3. Genera imágenes espejadas verticalmente:  
   Ejecuta el script `mirrorV.py` para generar versiones espejadas verticalmente de las imágenes y los archivos JSON:  
   python mirrorV.py  
   Esto creará una carpeta llamada `mirrorV` con las imágenes y JSON modificados.

4. Une todos los archivos en una carpeta:  
   Usa el script `merge_files.py` para combinar los archivos originales, horizontales y verticales en una carpeta llamada `images-json`:  
   python merge_files.py  

5. Convierte los JSON al formato YOLO OBB:  
   Ejecuta el script `json_to_yolo_obb.py` para generar las carpetas `images` y `labels` necesarias para el entrenamiento del modelo YOLO:  
   python json_to_yolo_obb.py  

### 2. Entrenamiento del modelo

1. Asegúrate de tener YOLOv11 instalado localmente.  
   Puedes seguir las instrucciones del repositorio oficial de YOLOv11 para configurarlo.  

2. Coloca las carpetas `images` y `labels` generadas en la estructura requerida por YOLO (dentro del directorio `datasets`).  

3. Configura el archivo de entrenamiento con los nombres de las clases y rutas correspondientes.  

4. Ejecuta el entrenamiento usando el siguiente comando en un entorno configurado con Anaconda:  
   python train.py --epochs <número_de_épocas> --data <ruta_a_tu_archivo_data.yaml> --weights yolov11.pt  

### 3. Detección de imágenes nuevas

1. Usa el archivo `best.pt` generado tras el entrenamiento para realizar detecciones en imágenes nuevas.  
   Ejecuta el siguiente comando:  
   python detect.py --weights best.pt --source <carpeta_o_imagen>  

2. Los resultados de las detecciones se guardarán automáticamente en la carpeta `runs/detect/`.

