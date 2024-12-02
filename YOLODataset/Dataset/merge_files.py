import os
import shutil

# Cambiar el directorio actual al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Directorios de origen
source_dirs = [
    "./LabelMe",
    "./mirrorH",
    "./mirrorV",
]

# Directorio de destino
output_dir = "./images-json"
os.makedirs(output_dir, exist_ok=True)

# Extensiones permitidas
valid_extensions = [".jpg", ".png", ".jpeg", ".json"]

# Función para copiar archivos sin sobrescribir
def copy_file_with_unique_name(src_path, dest_dir):
    base_name = os.path.basename(src_path)
    dest_path = os.path.join(dest_dir, base_name)
    counter = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(base_name)
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1
    shutil.copy(src_path, dest_path)

# Procesar cada carpeta de origen
for source_dir in source_dirs:
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        
        if os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1].lower()
            
            if ext in valid_extensions:
                copy_file_with_unique_name(file_path, output_dir)

print("Archivos combinados exitosamente.")
