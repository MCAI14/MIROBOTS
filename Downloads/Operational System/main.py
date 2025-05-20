import tkinter as tk
import subprocess
import os
from start import open_user_selection  # importa a função que cria a tela de utilizadores
from Programas.Default.Apps.Definições import open_definicoes
from Programas.Default.Apps.Calculadora import open_calculadora
from Programas.Default.Apps.EditorTexto import open_editor_texto

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ICONES_DIR = os.path.join(BASE_DIR, "icones")

def process_command(event):
    # Obtém o conteúdo da última linha começando no prompt (">> ")
    linha = terminal.get("insert linestart", "insert lineend")
    # Remove o prompt e espaços extras para isolar o comando
    comando = linha.replace(">> ", "", 1).strip().lower()
    
    if not comando:
        terminal.insert(tk.END, "\n>> ")
        terminal.see(tk.END)
        return "break"
    
    # Comandos personalizados do MIROBOTS
    if comando == "start mirobots":
        terminal.insert(tk.END, "\nCarregando MIRobots...\n")
        terminal.see(tk.END)
        load_mirobots()
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
        # Lista de comandos válidos para sugestão
        comandos_validos = [
            "start mirobots",
            "start calculadora",
            "start editor",
            "start definicoes",
            "start definições",
            "limpar",
            "ajuda",
            "shutdown",
            "reiniciar"
        ]

        # Função simples para sugerir comando parecido
        def sugerir_comando(comando_user):
            from difflib import get_close_matches
            sugestao = get_close_matches(comando_user, comandos_validos, n=1)
            return sugestao[0] if sugestao else None

        sugestao = sugerir_comando(comando)
        if sugestao:
            terminal.insert(tk.END, f'\nVocê disse "{comando}". Será que quis dizer "{sugestao}"?\nPara saber os comandos disponíveis, escreva "ajuda".')
        else:
            terminal.insert(tk.END, f'\nComando desconhecido: "{comando}". Para saber os comandos disponíveis, escreva "ajuda".')
    
    # Adiciona o prompt novamente
    terminal.insert(tk.END, "\n>> ")
    terminal.see(tk.END)
    return "break"

def load_mirobots():
    # Remove o terminal da janela
    terminal.pack_forget()
    
    # Cria um frame com fundo preto para a tela de inicialização
    splash = tk.Frame(janela, bg="black")
    splash.pack(expand=True, fill="both")
    
    # Tenta carregar a imagem do ícone personalizado
    try:
        icon_image = tk.PhotoImage(file=os.path.join(ICONES_DIR, "iconstart.png"))
    except Exception as e:
        print("Erro ao carregar a imagem do ícone:", e)
        icon_image = None

    # Exibe o ícone (se carregado) ou um texto alternativo no centro
    if icon_image:
        icon_label = tk.Label(splash, image=icon_image, bg="black")
        icon_label.image = icon_image  # Mantém a referência para não ser coletada
        icon_label.pack(pady=(100, 20))
    else:
        icon_label = tk.Label(splash, text="Ícone do MIRobots", font=("Consolas", 24), bg="black", fg="white")
        icon_label.pack(pady=(100, 20))
    
    # Cria um Label para simular uma rodinha de pensamento animada
    spinner_label = tk.Label(splash, text="", font=("Consolas", 24), bg="black", fg="white")
    spinner_label.pack(pady=(20, 0))
    
    # Lista de "frames" do spinner
    spinner_frames = ["|", "/", "-", "\\"]
    
    # Função que atualiza o spinner a cada 200ms
    def animate(index=0):
        spinner_label.config(text=spinner_frames[index % len(spinner_frames)])
        splash.after(200, animate, index+1)
    
    animate()
    
    # Após 5 segundos, chama a função de escolha de utilizadores
    splash.after(5000, lambda: open_user_selection(janela, splash))

# Cria a janela principal em tela cheia
janela = tk.Tk()
janela.title("Terminal")
janela.attributes("-fullscreen", True)

# Cria o widget Text que simula o terminal
terminal = tk.Text(janela, bg="black", fg="white", insertbackground="white", font=("Consolas", 14))
terminal.pack(expand=True, fill="both")

# Insere os direitos da MIRobots no início do terminal
direitos = """
MIRobots Operational System
Todos os direitos reservados © 2025 MIRobots Corporation & Pixel Corporation.
Proibida a reprodução total ou parcial sem autorização.
"""
terminal.insert(tk.END, direitos + "\n\n>> ")

# Associa o evento de pressionar Enter para processar o comando
terminal.bind("<Return>", process_command)

# Inicia o loop principal da interface
janela.mainloop()