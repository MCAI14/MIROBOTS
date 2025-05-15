import tkinter as tk
import os

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "icones")

def open_definicoes(janela):
    # Remove todos os widgets atuais da janela
    for widget in janela.winfo_children():
        widget.destroy()
    
    # Cria o frame principal para as definições
    frame = tk.Frame(janela, bg="lightgray")
    frame.pack(expand=True, fill="both")
    
    # Adiciona um título
    label = tk.Label(frame, text="Definições", font=("Consolas", 28), bg="lightgray", fg="black")
    label.pack(pady=20)
    
    # Adiciona informações ou configurações
    label_info = tk.Label(frame, text="Aqui você pode ajustar as configurações do sistema.", 
                          font=("Consolas", 14), bg="lightgray", fg="black")
    label_info.pack(pady=10)
    
    # Botão para voltar ao desktop
    voltar_btn = tk.Button(frame, text="Voltar", font=("Consolas", 14), bg="lightgray", fg="black",
                           command=lambda: voltar(janela))
    voltar_btn.pack(pady=20)

def voltar(janela):
    from users.guest import welcome
    welcome.open_desktop(janela)