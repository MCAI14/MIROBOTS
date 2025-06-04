import tkinter as tk
import subprocess
import sys
import os

# Dynamically add the parent directory of "Programas" to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from Programas.Default.Apps.Definições import open_definicoes
from Programas.Default.Apps.Calculadora import open_calculadora
from Programas.Default.Apps.EditorTexto import open_editor_texto
from Programas.Default.Apps.CodePode import open_codepode

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

# Guarda as janelas abertas
open_windows = {}

def open_desktop(janela):
    print("Iniciando ambiente de utilizador CONVIDADO")
    # Frame do ambiente de trabalho
    desktop = tk.Frame(janela, bg="deepskyblue")
    desktop.pack(expand=True, fill="both")

    # Frame da barra de tarefas (em baixo)
    taskbar = tk.Frame(desktop, bg="#222222", height=60)
    taskbar.pack(side="bottom", fill="x")

    # Lista de ícones na barra de tarefas
    taskbar_icons = {}

    def add_taskbar_icon(app_name, icon_path, win_ref):
        if app_name in taskbar_icons:
            return  # Já existe
        try:
            icon_img = tk.PhotoImage(file=icon_path)
        except Exception:
            icon_img = None
        btn = tk.Button(
            taskbar, image=icon_img, text=app_name, compound="top", bg="#222222", fg="white",
            font=("Consolas", 9), bd=0,
            command=lambda: restore_window(app_name)
        )
        btn.image = icon_img
        btn.pack(side="left", padx=5)
        taskbar_icons[app_name] = btn
        open_windows[app_name] = win_ref

    def remove_taskbar_icon(app_name):
        if app_name in taskbar_icons:
            taskbar_icons[app_name].destroy()
            del taskbar_icons[app_name]
        if app_name in open_windows:
            del open_windows[app_name]

    def restore_window(app_name):
        win = open_windows.get(app_name)
        if win:
            win.deiconify()
            win.lift()
            win.focus_force()

    # Exemplo para abrir Definições
    def open_definicoes_wrapper():
        win = tk.Toplevel(janela)
        win.title("Definições")
        win.protocol("WM_DELETE_WINDOW", lambda: [win.destroy(), remove_taskbar_icon("Definições")])
        win.iconphoto(True, tk.PhotoImage(file=os.path.join(ICONES_DIR, "Definições.png")))
        # ...restante código da janela...
        add_taskbar_icon("Definições", os.path.join(ICONES_DIR, "Definições.png"), win)
        # Para minimizar, só win.iconify()

    # Repete para Calculadora, EditorTexto, CodePode, etc.
    # Substitui os comandos dos botões da barra de tarefas para chamar estas wrappers

    # Exemplo de botão na barra de tarefas:
    btn_def = tk.Button(taskbar, text="Definições", command=open_definicoes_wrapper)
    btn_def.pack(side="left", padx=5)

    # Adiciona elementos ao desktop (menos a barra de tarefas)
    add_main_labels(desktop)

    # Adiciona botões/ícones à barra de tarefas
    add_taskbar_icons(taskbar)

def add_main_labels(desktop):
    # Adiciona os textos principais no desktop
    label1 = tk.Label(desktop, text="Divirta-se com esta versão!", font=("Consolas", 16, "bold"), 
                      bg="deepskyblue", fg="magenta")
    label1.place(x=50, y=50)

    label2 = tk.Label(desktop, text="Mais informações nas Definições", font=("Consolas", 14), 
                      bg="deepskyblue", fg="blue")
    label2.place(x=50, y=100)

    label3 = tk.Label(desktop, text="MIROBOTS 1.0\nVer. by Pixel Corporation\nLote 09032024\n2024", 
                      font=("Consolas", 16, "bold"), bg="deepskyblue", fg="magenta")
    label3.place(x=400, y=50)

def add_power_button(taskbar):
    power_img = tk.PhotoImage(file=os.path.join(ICONES_DIR, "Ligar-Desligar.png"))
    power_button = tk.Button(taskbar, image=power_img, bg="#222222", borderwidth=0,
                              command=lambda: open_power_options(taskbar.master))
    power_button.image = power_img  # Mantém a referência para não ser coletada
    power_button.pack(side="left", padx=10)

def add_taskbar_icons(taskbar):
    # Botão de power (primeiro)
    try:
        power_img = tk.PhotoImage(file=os.path.join(ICONES_DIR, "Ligar-Desligar.png"))
        power_button = tk.Button(taskbar, image=power_img, bg="#222222", borderwidth=0,
                                 command=lambda: open_power_options(taskbar.master))
        power_button.image = power_img
        power_button.pack(side="left", padx=10)
    except Exception as e:
        print(f"Erro ao carregar o ícone de power: {e}")

    # Outros ícones (pesquisa, definições, calculadora, etc.)
    try:
        search_img = tk.PhotoImage(file=os.path.join(ICONES_DIR, "Pesquisar.png"))
        search_button = tk.Button(taskbar, image=search_img, bg="#222222", borderwidth=0,
                                  command=lambda: open_pesquisa(taskbar.master))
        search_button.image = search_img
        search_button.pack(side="left", padx=10)
    except Exception as e:
        print(f"Erro ao carregar o ícone de pesquisa: {e}")

    icons = [
        (os.path.join(ICONES_DIR, "Definições.png"), open_definicoes),
        (os.path.join(ICONES_DIR, "Calculadora.png"), open_calculadora),
        (os.path.join(ICONES_DIR, "EditorTexto.png"), open_editor_texto),
        (os.path.join(ICONES_DIR, "CodePode.png"), open_codepode)
    ]
    for icon, command in icons:
        try:
            icon_img = tk.PhotoImage(file=icon)
            icon_button = tk.Button(taskbar, image=icon_img, bg="#222222", borderwidth=0,
                                     command=lambda cmd=command: cmd(taskbar.master))
            icon_button.image = icon_img
            icon_button.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar o ícone {icon}: {e}")

def open_power_options(parent):
    power_win = tk.Toplevel(parent)
    power_win.title("Opções de Energia")
    power_win.transient(None)
    power_win.attributes("-toolwindow", False)

    icon_path = os.path.join(ICONES_DIR, "Ligar-Desligar.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        power_win.iconphoto(True, icon_img)
        power_win._icon_img = icon_img
    except Exception as e:
        print("Erro ao definir o ícone de energia:", e)

    power_win.geometry("320x180+900+300")
    power_win.config(bg="white")

    label = tk.Label(power_win, text="O que pretende fazer?", font=("Consolas", 16, "bold"), bg="white")
    label.pack(pady=(20, 10))

    btn_frame = tk.Frame(power_win, bg="white")
    btn_frame.pack(pady=10)

    def encerrar():
        power_win.destroy()
        subprocess.run("shutdown /s /t 0", shell=True)

    def reiniciar():
        power_win.destroy()
        subprocess.run("shutdown /r /t 0", shell=True)

    def suspender():
        power_win.destroy()
        subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True)

    btn_encerrar = tk.Button(btn_frame, text="Encerrar", font=("Consolas", 12), width=10, command=encerrar, bg="#ff5555", fg="white")
    btn_encerrar.grid(row=0, column=0, padx=10)

    btn_reiniciar = tk.Button(btn_frame, text="Reiniciar", font=("Consolas", 12), width=10, command=reiniciar, bg="#ffaa00", fg="white")
    btn_reiniciar.grid(row=0, column=1, padx=10)

    btn_suspender = tk.Button(btn_frame, text="Suspender", font=("Consolas", 12), width=10, command=suspender, bg="#55aaff", fg="white")
    btn_suspender.grid(row=0, column=2, padx=10)

    btn_cancelar = tk.Button(power_win, text="Cancelar", font=("Consolas", 12), width=10, command=power_win.destroy)
    btn_cancelar.pack(pady=10)

def shutdown(option):
    try:
        if option == "encerrar":
            subprocess.run("shutdown /s /t 0", shell=True, check=True)
        elif option == "suspender":
            subprocess.run("shutdown /h", shell=True, check=True)
        elif option == "reiniciar":
            subprocess.run("shutdown /r /t 0", shell=True, check=True)
    except Exception as e:
        print(f"Erro ao executar o comando de energia: {e}")

def open_pesquisa(parent):
    # Exemplo: abre uma janela de pesquisa (podes adaptar)
    pesquisa_win = tk.Toplevel(parent)
    pesquisa_win.title("Pesquisar")
    pesquisa_win.transient(None)
    pesquisa_win.attributes("-toolwindow", False)

    pesquisa_win.geometry("300x100+850+200")
    pesquisa_win.config(bg="white")
    entry = tk.Entry(pesquisa_win, font=("Consolas", 14))
    entry.pack(pady=20, padx=20, fill="x")