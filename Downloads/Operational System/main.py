import tkinter as tk
import os
import sys

from start import open_user_selection

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "users", "guest")))

try:
    from Programas.Default.Apps.Definições import open_definicoes
except ImportError:
    def open_definicoes(janela): pass

try:
    from Programas.Default.Apps.Calculadora import open_calculadora
except ImportError:
    def open_calculadora(janela): pass

try:
    from Programas.Default.Apps.EditorTexto import open_editor_texto
except ImportError:
    def open_editor_texto(janela): pass

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ICONES_DIR = os.path.join(BASE_DIR, "icones")

# Cria a janela principal em tela cheia
janela = tk.Tk()
janela.title("MIRobots")
janela.attributes("-fullscreen", True)

# Splash inicial com ícone
def show_splash():
    splash = tk.Frame(janela, bg="black")
    splash.pack(expand=True, fill="both")

    # Tenta carregar o ícone
    try:
        icon_image = tk.PhotoImage(file=os.path.join(ICONES_DIR, "iconstart.png"))
    except Exception as e:
        print("Erro ao carregar a imagem do ícone:", e)
        icon_image = None

    if icon_image:
        icon_label = tk.Label(splash, image=icon_image, bg="black")
        icon_label.image = icon_image
        icon_label.pack(pady=(100, 20))
    # Se não houver ícone, não mostra nada (nem texto)

    spinner_label = tk.Label(splash, text="", font=("Consolas", 24), bg="black", fg="white")
    spinner_label.pack(pady=(20, 0))
    spinner_frames = ["|", "/", "-", "\\"]
    def animate(index=0):
        spinner_label.config(text=spinner_frames[index % len(spinner_frames)])
        splash.after(200, animate, index+1)
    animate()

    # Texto no canto inferior esquerdo
    esc_label = tk.Label(
        splash, text="Press ESC to access the Terminal", font=("Consolas", 12),
        bg="black", fg="#aaa"
    )
    esc_label.place(relx=0.01, rely=0.97, anchor="sw")

    # Função para aceder ao terminal ao pressionar ESC
    def on_esc(event):
        open_terminal(splash)
    splash.bind_all("<Escape>", on_esc)

    # Após 5 segundos, avança para o ambiente gráfico se não clicar em ESC
    splash.after(5000, lambda: open_user_selection(janela, splash))

def open_terminal(splash):
    splash.destroy()
    # Terminal clássico
    terminal = tk.Text(janela, bg="black", fg="white", insertbackground="white", font=("Consolas", 14))
    terminal.pack(expand=True, fill="both")
    direitos = """
MIRobots Operational System
Todos os direitos reservados © 2025 MIRobots Corporation & Pixel Corporation.
Proibida a reprodução total ou parcial sem autorização.
"""
    terminal.insert(tk.END, direitos + "\n\n>> ")

    def process_command(event=None):
        linha = terminal.get("insert linestart", "insert lineend")
        comando = linha.replace(">> ", "", 1).strip().lower()
        if not comando:
            terminal.insert(tk.END, "\n>> ")
            terminal.see(tk.END)
            return "break"
        if comando == "start mirobots":
            terminal.insert(tk.END, "\nCarregando MIRobots...\n")
            terminal.see(tk.END)
            terminal.pack_forget()
            show_splash()
        elif comando == "start calculadora":
            open_calculadora(janela)
            terminal.insert(tk.END, "\nCalculadora aberta.\n")
        elif comando == "start editor":
            open_editor_texto(janela)
            terminal.insert(tk.END, "\nEditor de texto aberto.\n")
        elif comando == "start definicoes" or comando == "start definições":
            open_definicoes(janela)
            terminal.insert(tk.END, "\nDefinições abertas.\n")
        elif comando == "limpar":
            terminal.delete("1.0", tk.END)
            terminal.insert(tk.END, ">> ")
        elif comando == "ajuda":
            terminal.insert(tk.END, """
Comandos disponíveis:
start mirobots      - Inicia o ambiente gráfico
start calculadora   - Abre a calculadora
start editor        - Abre o editor de texto
start definicoes    - Abre as definições
limpar              - Limpa o terminal
ajuda               - Mostra esta ajuda
shutdown            - Desliga o computador
reiniciar           - Reinicia o computador

Também pode escrever comandos do Windows, como: dir, cls, echo, ping, etc.
""")
        elif comando == "shutdown":
            terminal.insert(tk.END, "\nA desligar o computador...\n")
            terminal.see(tk.END)
            os.system("shutdown /s /t 0")
        elif comando == "reiniciar":
            terminal.insert(tk.END, "\nA reiniciar o computador...\n")
            terminal.see(tk.END)
            os.system("shutdown /r /t 0")
        else:
            terminal.insert(tk.END, f'\nComando desconhecido: "{comando}". Para saber os comandos disponíveis, escreva "ajuda".')
        terminal.insert(tk.END, "\n>> ")
        terminal.see(tk.END)
        return "break"

    terminal.bind("<Return>", process_command)

# Inicia o splash logo ao abrir
show_splash()

# Inicia o loop principal da interface
janela.mainloop()