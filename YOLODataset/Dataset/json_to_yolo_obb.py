import os
import json
import shutil
import random

# Cambiar el directorio actual al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Directorios de entrada y salida
input_dir = "./images-json"
output_dir = "C:/Users/.../YOLODataset" #Ruta a carpeta YOLODataset
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, "images/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images/val"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/val"), exist_ok=True)

train_ratio = 0.8
json_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]
image_extensions = [".jpg", ".png", ".jpeg"]

# Mezclar y dividir en conjuntos de entrenamiento y validación
random.shuffle(json_files)
train_count = int(len(json_files) * train_ratio)
train_files = json_files[:train_count]
val_files = json_files[train_count:]

def normalize_points(points, image_width, image_height):
    return [(x / image_width, y / image_height) for x, y in points]

for phase, files in zip(["train", "val"], [train_files, val_files]):
    for json_file in files:
        with open(os.path.join(input_dir, json_file), "r") as f:
            data = json.load(f)

        image_width = data["imageWidth"]
        image_height = data["imageHeight"]
        labels = []

        for shape in data["shapes"]:
            label = shape["label"]
            points = shape["points"]
            
            if len(points) == 4:  # Asegurar que son 4 puntos
                normalized_points = normalize_points(points, image_width, image_height)
                flattened_points = [coord for point in normalized_points for coord in point]
                labels.append(f"0 " + " ".join(map(str, flattened_points)))

        # Escribir archivo de etiquetas
        label_file = os.path.join(output_dir, f"labels/{phase}", json_file.replace(".json", ".txt"))
        with open(label_file, "w") as out_f:
            out_f.write("\n".join(labels))
        
        # Buscar y copiar la imagen correspondiente
        image_file = None
        for ext in image_extensions:
            potential_image = os.path.join(input_dir, json_file.replace(".json", ext))
            if os.path.exists(potential_image):
                image_file = potential_image
                break
        
        if image_file:
            shutil.copy(image_file, os.path.join(output_dir, f"images/{phase}"))
        else:
            print(f"Imagen no encontrada para {json_file}. Verifica las extensiones.")

print("Conversión a formato YOLO OBB completada.")
