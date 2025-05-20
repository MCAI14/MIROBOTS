import tkinter as tk
import os

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

def open_definicoes(parent):
    # Cria uma nova janela (Toplevel)
    def_win = tk.Toplevel(parent)
    def_win.title("Definições")
    icon_path = os.path.join(ICONES_DIR, "Definições.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        def_win.iconphoto(True, icon_img)
        def_win._icon_img = icon_img
    except Exception as e:
        print("Erro ao definir o ícone das definições:", e)

    def_win.geometry("400x250+850+200")
    def_win.config(bg="white")

    # Título
    label = tk.Label(def_win, text="Definições", font=("Consolas", 20, "bold"), bg="white", fg="black")
    label.pack(pady=20)

    # Informação
    info = tk.Label(def_win, text="Aqui pode ajustar as configurações do sistema.", 
                    font=("Consolas", 14), bg="white", fg="black")
    info.pack(pady=10)

    # Botão para fechar
    btn = tk.Button(def_win, text="Fechar", font=("Consolas", 12), command=def_win.destroy)
    btn.pack(pady=20)

def voltar(janela):
    from users.guest import welcome
    welcome.open_desktop(janela)