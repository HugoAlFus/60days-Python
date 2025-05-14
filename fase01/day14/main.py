import os
import shutil

directory = "../../assets/example"

file_type = {
    "imagenes": [".jpg", ".png", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "otros": [".py", ".json", ".log", ".csv"]
}

for folder in file_type:
    path_folder = os.path.join(directory, folder)
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)

for file in os.listdir(directory):
    path_file = os.path.join(directory, file)

    if os.path.isfile(path_file):
        _, extension = os.path.splitext(file)

        move = False
        for category, extensions in file_type.items():
            if extension.lower() in extensions:
                shutil.move(path_file, os.path.join(directory, category, file))
                print(f"Movido {file} -> {category}")
                move = True
                break
