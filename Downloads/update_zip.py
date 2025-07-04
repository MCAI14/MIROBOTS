import zipfile
import os

if os.path.exists("MIROBOTS.zip"):
    os.remove("MIROBOTS.zip")

zip_path = "MIROBOTS.zip"
folder_to_add = "Operational System"

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_add):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(folder_to_add))
            zipf.write(file_path, arcname)