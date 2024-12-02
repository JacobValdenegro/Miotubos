import os
import json
import cv2

# Cambiar el directorio actual al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configura tus carpetas
input_dir = "./LabelMe"  # Carpeta de entrada con imágenes y JSON
output_dir = "./mirrorV"  # Carpeta de salida

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Procesar todos los archivos JSON en la carpeta
for file_name in os.listdir(input_dir):
    if file_name.endswith(".json"):  # Filtrar solo archivos JSON
        # Ruta completa del JSON
        json_path = os.path.join(input_dir, file_name)

        # Leer el archivo JSON
        with open(json_path, 'r') as f:
            data = json.load(f)

        # Ruta completa de la imagen asociada
        image_name = data["imagePath"]
        image_path = os.path.join(input_dir, image_name)

        # Leer la imagen para obtener la altura
        image = cv2.imread(image_path)
        if image is None:
            print(f"Imagen no encontrada: {image_path}")
            continue

        img_height = image.shape[0]  # Altura de la imagen

        # Crear espejo de la imagen
        mirrored_image = cv2.flip(image, 0)  # Flip vertical

        # Ajustar las anotaciones
        for shape in data["shapes"]:
            original_points = shape["points"]
            mirrored_points = [[x, img_height - y] for x, y in original_points]  # Reflejar Y
            shape["points"] = mirrored_points  # Actualizar los puntos en el JSON

        # Modificar el nombre de la imagen y del JSON en los datos
        mirrored_image_name = f"mirrored_v_{image_name}"
        mirrored_json_name = f"mirrored_v_{file_name}"
        data["imagePath"] = mirrored_image_name

        # Guardar la imagen espejada
        mirrored_image_path = os.path.join(output_dir, mirrored_image_name)
        cv2.imwrite(mirrored_image_path, mirrored_image)

        # Guardar el JSON actualizado
        mirrored_json_path = os.path.join(output_dir, mirrored_json_name)
        with open(mirrored_json_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Procesado: {file_name} -> {mirrored_json_name}")

print("Duplicado de imágenes y JSON completado.")
