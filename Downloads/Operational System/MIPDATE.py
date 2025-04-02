import os
import requests
import json

# Caminho para o arquivo local de versão
LOCAL_VERSION_FILE = "version.txt"

# URL do servidor de atualizações
UPDATE_INFO_URL = "http://example.com/updates/update_info.json"

def get_local_version():
    """Lê a versão local do arquivo version.txt."""
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0.0"  # Versão inicial padrão
    with open(LOCAL_VERSION_FILE, "r") as file:
        return file.read().strip()

def set_local_version(version):
    """Atualiza a versão local no arquivo version.txt."""
    with open(LOCAL_VERSION_FILE, "w") as file:
        file.write(version)

def check_for_updates():
    """Verifica se há atualizações disponíveis no servidor."""
    try:
        response = requests.get(UPDATE_INFO_URL)
        if response.status_code == 200:
            update_info = response.json()
            return update_info
        else:
            print("Erro ao verificar atualizações:", response.status_code)
            return None
    except Exception as e:
        print("Erro ao conectar ao servidor de atualizações:", e)
        return None

def download_file(url, dest):
    """Faz o download de um arquivo do servidor."""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(dest, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Arquivo baixado: {dest}")
        else:
            print(f"Erro ao baixar {url}: {response.status_code}")
    except Exception as e:
        print(f"Erro ao baixar {url}:", e)

def apply_updates(update_info):
    """Aplica as atualizações baixando os arquivos necessários."""
    for file_info in update_info["files"]:
        file_name = file_info["name"]
        file_url = file_info["url"]
        print(f"Baixando {file_name}...")
        download_file(file_url, file_name)
    print("Atualizações aplicadas com sucesso!")

def main():
    print("Verificando atualizações...")
    local_version = get_local_version()
    update_info = check_for_updates()

    if update_info and update_info["version"] != local_version:
        print(f"Nova versão disponível: {update_info['version']}")
        apply_updates(update_info)
        set_local_version(update_info["version"])
        print("Sistema atualizado para a versão mais recente!")
    else:
        print("Nenhuma atualização disponível.")

if __name__ == "__main__":
    main()