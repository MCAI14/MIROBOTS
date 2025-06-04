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

janela = tk.Tk()
janela.title("MIRobots")
janela.attributes("-fullscreen", True)

def show_splash():
    splash = tk.Frame(janela, bg="#000080")  # azul escuro retro
    splash.pack(expand=True, fill="both")

    # Ícone pixelizado (ou texto se não houver)
    try:
        icon_image = tk.PhotoImage(file=os.path.join(ICONES_DIR, "iconstart.png"))
        icon_label = tk.Label(splash, image=icon_image, bg="#000080")
        icon_label.image = icon_image
        icon_label.pack(pady=(100, 20))
    except Exception:
        icon_label = tk.Label(splash, text="MIRobots", font=("Consolas", 40, "bold"), bg="#000080", fg="#00ff00")
        icon_label.pack(pady=(100, 20))

    # Spinner retro
    spinner_label = tk.Label(splash, text="LOADING █▒▒▒▒▒▒▒▒", font=("Consolas", 24), bg="#000080", fg="#00ff00")
    spinner_label.pack(pady=(20, 0))
    def animate(step=0):
        bar = "█" + "▒" * (step % 9) + " " * (8 - (step % 9))
        spinner_label.config(text=f"LOADING {bar}")
        splash.after(180, animate, step+1)
    animate()

    # Texto no canto inferior esquerdo
    esc_label = tk.Label(
        splash, text="Press ESC for the Terminal (old school!)", font=("Consolas", 12),
        bg="#000080", fg="#ff00ff"
    )
    esc_label.place(relx=0.01, rely=0.97, anchor="sw")

    def on_esc(event):
        open_terminal(splash)
    splash.bind_all("<Escape>", on_esc)

    splash.after(3500, lambda: open_user_selection(janela, splash))

def open_terminal(splash):
    splash.destroy()
    terminal = tk.Text(janela, bg="#111", fg="#0f0", insertbackground="#0f0", font=("Consolas", 14), borderwidth=8, relief="ridge")
    terminal.pack(expand=True, fill="both")
    direitos = """
MIRobots DOS Terminal
(c) 2025 MIRobots Corporation & Pixel Corp.
Type 'ajuda' for help.
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
            terminal.insert(tk.END, f'\nComando desconhecido: "{comando}". Escreva "ajuda".')
        terminal.insert(tk.END, "\n>> ")
        terminal.see(tk.END)
        return "break"

    terminal.bind("<Return>", process_command)

def open_desktop(janela):
    # Fundo azul ciano forte
    desktop = tk.Frame(janela, bg="#00cfff")
    desktop.pack(expand=True, fill="both")

    # Dashboard quadrado e widgets quadrados
    dashboard = tk.Frame(desktop, bg="#222", bd=4, relief="groove")
    dashboard.place(relx=0.5, rely=0.45, anchor="center", width=800, height=400)

    # Widgets quadrados, cores fortes
    widget1 = tk.Frame(dashboard, bg="#ff00ff", bd=2, relief="ridge")
    widget1.place(x=30, y=30, width=180, height=120)
    tk.Label(widget1, text="Photos", font=("Consolas", 13, "bold"), bg="#ff00ff", fg="#fff").pack(anchor="nw", padx=10, pady=8)

    widget2 = tk.Frame(dashboard, bg="#00ffea", bd=2, relief="ridge")
    widget2.place(x=230, y=30, width=180, height=120)
    tk.Label(widget2, text="Reminders", font=("Consolas", 13, "bold"), bg="#00ffea", fg="#000").pack(anchor="nw", padx=10, pady=8)

    widget3 = tk.Frame(dashboard, bg="#fff700", bd=2, relief="ridge")
    widget3.place(x=430, y=30, width=180, height=120)
    tk.Label(widget3, text="Calendar", font=("Consolas", 13, "bold"), bg="#fff700", fg="#000").pack(anchor="nw", padx=10, pady=8)

    widget4 = tk.Frame(dashboard, bg="#ff5e00", bd=2, relief="ridge")
    widget4.place(x=630, y=30, width=140, height=120)
    tk.Label(widget4, text="Performance", font=("Consolas", 13, "bold"), bg="#ff5e00", fg="#fff").pack(anchor="nw", padx=10, pady=8)

    # Barra de tarefas tipo DOS/retro
    taskbar = tk.Frame(desktop, bg="#111", height=48, bd=4, relief="ridge")
    taskbar.pack(side="bottom", fill="x")
    for i, nome in enumerate(["Definições", "Calc", "Editor", "Code"]):
        btn = tk.Button(taskbar, text=nome, font=("Consolas", 12, "bold"), bg="#222", fg="#0ff", bd=2, relief="groove", width=12, height=1, cursor="hand2")
        btn.pack(side="left", padx=8, pady=4)

show_splash()
janela.mainloop()