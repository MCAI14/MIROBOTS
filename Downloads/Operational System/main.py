import tkinter as tk
import subprocess
from start import open_user_selection  # importa a função que cria a tela de utilizadores

def process_command(event):
    # Obtém o conteúdo da última linha começando no prompt (">> ")
    linha = terminal.get("insert linestart", "insert lineend")
    # Remove o prompt e espaços extras para isolar o comando
    comando = linha.replace(">> ", "", 1).strip()
    
    if comando.lower() == "start mirobots":
        terminal.insert(tk.END, "\nCarregando MIRobots...\n")
        terminal.see(tk.END)
        load_mirobots()
    else:
        try:
            # Executa o comando no sistema operacional
            resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
            # Exibe a saída do comando no terminal
            if resultado.stdout:
                terminal.insert(tk.END, "\n" + resultado.stdout)
            if resultado.stderr:
                terminal.insert(tk.END, "\n" + resultado.stderr)
        except Exception as e:
            terminal.insert(tk.END, f"\nErro ao executar o comando: {e}")
    
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
        icon_image = tk.PhotoImage(file="iconstart.png")
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
    splash.after(5000, lambda: open_user_selection(janela, splash))  # Fixed missing parenthesis

# Cria a janela principal em tela cheia
janela = tk.Tk()
janela.title("Terminal")
janela.attributes("-fullscreen", True)

# Cria o widget Text que simula o terminal
terminal = tk.Text(janela, bg="black", fg="white", insertbackground="white", font=("Consolas", 14))
terminal.pack(expand=True, fill="both")

# Insere o prompt inicial
terminal.insert(tk.END, ">> ")

# Associa o evento de pressionar Enter para processar o comando
terminal.bind("<Return>", process_command)

# Inicia o loop principal da interface
janela.mainloop()