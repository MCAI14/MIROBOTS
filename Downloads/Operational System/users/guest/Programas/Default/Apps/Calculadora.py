import tkinter as tk
import os

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

def open_calculadora(janela):
    # Remove todos os widgets atuais da janela
    for widget in janela.winfo_children():
        widget.destroy()
    
    # Cria o frame principal para a calculadora
    frame = tk.Frame(janela, bg="white")
    frame.pack(expand=True, fill="both")
    
    # Adiciona um título
    label = tk.Label(frame, text="Calculadora", font=("Consolas", 28), bg="white", fg="black")
    label.pack(pady=20)
    
    # Campo de entrada para os números
    entry = tk.Entry(frame, font=("Consolas", 14), justify="right")
    entry.pack(pady=10, padx=20, fill="x")
    
    # Função para calcular a expressão
    def calcular():
        try:
            resultado = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(resultado))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Erro")
    
    # Botão para calcular
    calc_btn = tk.Button(frame, text="Calcular", font=("Consolas", 14), bg="lightgray", fg="black",
                         command=calcular)
    calc_btn.pack(pady=10)
    
    # Botão para voltar ao desktop
    voltar_btn = tk.Button(frame, text="Voltar", font=("Consolas", 14), bg="lightgray", fg="black",
                           command=lambda: voltar(janela))
    voltar_btn.pack(pady=20)

def voltar(janela):
    from users.guest import welcome
    welcome.open_desktop(janela)