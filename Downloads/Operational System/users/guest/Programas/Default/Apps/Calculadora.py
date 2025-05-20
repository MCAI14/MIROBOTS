import tkinter as tk
import os
import math

# Caminho absoluto para a pasta 'icones' na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

def open_calculadora(parent, fullscreen=False):
    calc_win = tk.Toplevel(parent)
    calc_win.title("Calculadora Científica")
    icon_path = os.path.join(ICONES_DIR, "Calculadora.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        calc_win.iconphoto(True, icon_img)
        calc_win._icon_img = icon_img  # Mantém referência!
    except Exception as e:
        print("Erro ao definir o ícone da calculadora:", e)
    if fullscreen:
        calc_win.geometry("700x520+400+100")
    else:
        calc_win.geometry("420x520+900+200")
    calc_win.config(bg="white")

    main_frame = tk.Frame(calc_win, bg="white")
    main_frame.pack(expand=True, fill="both")

    # Se fullscreen, adiciona frame para histórico
    if fullscreen:
        left_frame = tk.Frame(main_frame, bg="white")
        left_frame.pack(side="left", fill="both", expand=True)
        right_frame = tk.Frame(main_frame, bg="#f5f5f5", width=250)
        right_frame.pack(side="right", fill="y")
        history_label = tk.Label(right_frame, text="Histórico", font=("Consolas", 14, "bold"), bg="#f5f5f5")
        history_label.pack(pady=(10, 0))
        history_box = tk.Text(right_frame, font=("Consolas", 12), bg="#f5f5f5", state="disabled", width=28, height=30)
        history_box.pack(padx=10, pady=10, fill="y")
        frame = left_frame
    else:
        frame = main_frame
        history_box = None

    entry = tk.Entry(frame, font=("Consolas", 18), justify="right", bd=3, relief="sunken")
    entry.pack(pady=15, padx=10, fill="x")

    # Dicionário seguro de funções matemáticas
    safe_dict = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "log": math.log10,
        "ln": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "pow": math.pow,
        "abs": abs,
        "round": round,
        "exp": math.exp,
        "deg": math.degrees,
        "rad": math.radians,
        "__builtins__": {}
    }

    def inserir(valor):
        entry.insert(tk.END, valor)

    def limpar():
        entry.delete(0, tk.END)

    def calcular():
        try:
            expr = entry.get().replace("^", "**")
            resultado = eval(expr, safe_dict)
            entry.delete(0, tk.END)
            entry.insert(0, str(resultado))
            if history_box:
                history_box.config(state="normal")
                history_box.insert(tk.END, f"{expr} = {resultado}\n")
                history_box.see(tk.END)
                history_box.config(state="disabled")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Erro")

    # Layout dos botões (linha a linha)
    botoes = [
        ["7", "8", "9", "/", "(", ")", "sqrt"],
        ["4", "5", "6", "*", "pi", "e", "pow"],
        ["1", "2", "3", "-", "sin", "cos", "tan"],
        ["0", ".", ",", "+", "log", "ln", "^"],
        ["C", "abs", "exp", "deg", "rad", "=", "Fechar"]
    ]

    funcoes = {
        "sin": lambda: inserir("sin("),
        "cos": lambda: inserir("cos("),
        "tan": lambda: inserir("tan("),
        "asin": lambda: inserir("asin("),
        "acos": lambda: inserir("acos("),
        "atan": lambda: inserir("atan("),
        "log": lambda: inserir("log("),
        "ln": lambda: inserir("ln("),
        "sqrt": lambda: inserir("sqrt("),
        "pi": lambda: inserir("pi"),
        "e": lambda: inserir("e"),
        "pow": lambda: inserir("pow("),
        "abs": lambda: inserir("abs("),
        "exp": lambda: inserir("exp("),
        "deg": lambda: inserir("deg("),
        "rad": lambda: inserir("rad("),
        "^": lambda: inserir("^"),
        "C": limpar,
        "=": calcular,
        "Fechar": calc_win.destroy,
        ",": lambda: inserir("."),
    }

    # Criação dos botões
    for i, linha in enumerate(botoes):
        row = tk.Frame(frame, bg="white")
        row.pack(fill="x", padx=5, pady=2)
        for btn in linha:
            action = funcoes.get(btn, lambda b=btn: inserir(b))
            tk.Button(
                row, text=btn, width=5, height=2, font=("Consolas", 13),
                command=action, bg="#f0f0f0" if btn != "=" else "#b0e0b0"
            ).pack(side="left", padx=2, pady=2)

    # Atalho para Enter = calcular
    calc_win.bind("<Return>", lambda e: calcular())