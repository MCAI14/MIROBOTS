import tkinter as tk
import os
import subprocess  # Adicione esta importação

def open_desktop(janela):
    print("Iniciando ambiente de utilizador CONVIDADO")
    # Cria um frame que simula o ambiente de trabalho do Windows 1.0
    desktop = tk.Frame(janela, bg="gray")
    desktop.pack(expand=True, fill="both")
    
    # Adiciona um Label de boas-vindas
    welcome_label = tk.Label(desktop, text="Bem-vindo ao MIRobots Desktop - Convidado", 
                             font=("Consolas", 28), bg="gray", fg="white")
    welcome_label.pack(pady=50)
    
    # Adiciona o botão "Jogos" no desktop, redirecionando para Programas/Jogos/Jogos.py
    jogos_btn = tk.Button(desktop, text="Jogos", font=("Consolas", 14), 
                          bg="lightgray", fg="black", command=lambda: abre_jogos(janela))
    jogos_btn.pack(pady=20)
    
    # Crie a imagem como um objeto PhotoImage e mantenha a referência
    ligar_img = tk.PhotoImage(file="Ligar-Desligar.png")
    
    # Cria um botão de desligar no canto inferior esquerdo com a imagem "Ligar-Desligar.png"
    power_button = tk.Button(desktop, image=ligar_img, font=("Consolas", 20),
                             bg="gray", fg="white",
                             command=lambda: open_power_options(desktop))
    power_button.image = ligar_img  # Mantém a referência para não ser coletada
    # Posiciona o botão no canto inferior esquerdo com uma margem
    power_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)

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
            # Execute o arquivo shutdown.bat
            subprocess.run(["shutdown.bat"], check=True, shell=True)
        elif option == "suspender":
            # Use o comando para suspender o computador
            subprocess.run("shutdown /h", check=True, shell=True)
        elif option == "reiniciar":
            # Execute o arquivo restart.bat
            subprocess.run(["restart.bat"], check=True, shell=True)
    except FileNotFoundError as e:
        print(f"Arquivo .bat não encontrado: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def abre_jogos(janela):
    print("Abrindo a área de Jogos...")
    try:
        # Importa a função open_jogos do módulo Jogos.py (certifique-se de que a estrutura de pastas esteja correta)
        from users.guest.Programas.Jogos import Jogos
        Jogos.open_jogos(janela)
    except Exception as e:
        print("Erro ao abrir Jogos:", e)

    # Adicione mais botões ou funcionalidades conforme necessário