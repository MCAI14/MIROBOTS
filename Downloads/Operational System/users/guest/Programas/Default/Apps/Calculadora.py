import tkinter as tk
import os

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

def open_calculadora(parent):
    calc_win = tk.Toplevel(parent)
    calc_win.title("Calculadora")
    calc_win.geometry("350x350+900+250")
    calc_win.config(bg="white")

    # Frame principal
    frame = tk.Frame(calc_win, bg="white")
    frame.pack(expand=True, fill="both")

    # Título
    label = tk.Label(frame, text="Calculadora", font=("Consolas", 28), bg="white", fg="black")
    label.pack(pady=20)

    # Campo de entrada
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

    # Botão para fechar a calculadora
    fechar_btn = tk.Button(frame, text="Fechar", font=("Consolas", 14), bg="lightgray", fg="black",
                           command=calc_win.destroy)
    fechar_btn.pack(pady=20)