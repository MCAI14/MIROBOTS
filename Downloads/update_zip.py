import zipfile
import os

zip_path = "MIROBOTS.zip"
folder_to_add = "Operational System"

# Cria um novo ZIP sobrescrevendo o anterior
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_add):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(folder_to_add))
            zipf.write(file_path, arcname)