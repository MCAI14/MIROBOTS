import tkinter as tk
import subprocess

def open_desktop(janela):
    print("Iniciando ambiente de utilizador CONVIDADO")
    # Cria um frame que simula o ambiente de trabalho
    desktop = tk.Frame(janela, bg="deepskyblue")
    desktop.pack(expand=True, fill="both")
    
    # Adiciona os elementos principais no desktop
    add_main_labels(desktop)
    add_power_button(desktop)
    add_taskbar_icons(desktop)

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

def add_power_button(desktop):
    # Adiciona o botão de desligar no canto inferior esquerdo
    power_img = tk.PhotoImage(file="Ligar-Desligar.png")
    power_button = tk.Button(desktop, image=power_img, bg="deepskyblue", borderwidth=0,
                              command=lambda: open_power_options(desktop))
    power_button.image = power_img  # Mantém a referência para não ser coletada
    power_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

def add_taskbar_icons(desktop):
    # Adiciona ícones na barra de tarefas
    icons = ["icon1.png", "icon2.png", "icon3.png", "icon4.png", "icon5.png", "icon6.png"]
    x_offset = 50
    for icon in icons:
        try:
            icon_img = tk.PhotoImage(file=icon)
            icon_button = tk.Button(desktop, image=icon_img, bg="deepskyblue", borderwidth=0)
            icon_button.image = icon_img  # Mantém a referência para não ser coletada
            icon_button.place(x=x_offset, y=450)  # Ajuste a posição conforme necessário
            x_offset += 70
        except Exception as e:
            print(f"Erro ao carregar o ícone {icon}: {e}")

def open_power_options(parent):
    # Cria uma janela (Toplevel) separada para as opções de energia
    options_win = tk.Toplevel(parent)
    options_win.title("Opções de Energia")
    options_win.geometry("200x200+800+100")
    options_win.config(bg="lightgray")
    
    # Botão para "Encerrar" (executa um .bat)
    shutdown_btn = tk.Button(options_win, text="Encerrar", font=("Consolas", 14),
                             command=lambda: shutdown("encerrar"))
    # Botão para "Suspender" (suspende o computador)
    suspend_btn = tk.Button(options_win, text="Suspender", font=("Consolas", 14),
                            command=lambda: shutdown("suspender"))
    # Botão para "Reiniciar" (reinicia o computador)
    restart_btn = tk.Button(options_win, text="Reiniciar", font=("Consolas", 14),
                            command=lambda: shutdown("reiniciar"))
    
    shutdown_btn.pack(fill="x", pady=5, padx=10)
    suspend_btn.pack(fill="x", pady=5, padx=10)
    restart_btn.pack(fill="x", pady=5, padx=10)

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