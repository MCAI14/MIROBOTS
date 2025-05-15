import tkinter as tk
import os

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ICONES_DIR = os.path.join(BASE_DIR, "icones")

def open_user_selection(janela, splash):
    # Remove a tela de inicialização
    splash.destroy()
    
    # Cria um novo frame para a escolha de utilizadores
    user_selection_frame = tk.Frame(janela, bg="lightblue")
    user_selection_frame.pack(expand=True, fill="both")
    
    # Adiciona um Label simples com a mensagem para seleção
    label = tk.Label(user_selection_frame, text="Selecione o utilizador", font=("Consolas", 24), bg="lightblue", fg="black")
    label.pack(pady=20)
    
    # Cria um botão para o utilizador CONVIDADO
    guest_button = tk.Button(user_selection_frame, text="CONVIDADO", font=("Consolas", 20),
                             command=lambda: load_guest(janela, user_selection_frame))
    guest_button.pack(pady=20)

def load_guest(janela, current_frame):
    # Remove o frame atual da escolha de utilizadores
    current_frame.destroy()
    
    # Importa e chama o ambiente de trabalho do utilizador convidado (welcome.py)
    try:
        from users.guest import welcome
        welcome.open_desktop(janela)
    except Exception as e:
        print("Erro ao carregar o ambiente do utilizador CONVIDADO:", e)