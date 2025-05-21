import tkinter as tk
import os
import json
import hashlib

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")
USERS_FILE = os.path.join(BASE_DIR, "users.json")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"CONVIDADO": {"password": "", "admin": False}}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

def open_definicoes(parent):
    def_win = tk.Toplevel(parent)
    def_win.title("Definições")
    icon_path = os.path.join(ICONES_DIR, "Definições.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        def_win.iconphoto(True, icon_img)
        def_win._icon_img = icon_img
    except Exception as e:
        print("Erro ao definir o ícone das definições:", e)

    def_win.geometry("700x400+850+200")
    def_win.config(bg="#f6fcf6")

    # --- Menu lateral ---
    sidebar = tk.Frame(def_win, bg="#eaf6ea", width=180)
    sidebar.pack(side="left", fill="y")

    main_area = tk.Frame(def_win, bg="white")
    main_area.pack(side="right", expand=True, fill="both")

    # Botões do menu lateral
    def show_base():
        for widget in main_area.winfo_children():
            widget.destroy()
        tk.Label(main_area, text="Base", font=("Consolas", 20, "bold"), bg="white").pack(pady=20)
        tk.Label(main_area, text="Definições gerais do sistema.", font=("Consolas", 14), bg="white").pack(pady=10)

    def show_users():
        for widget in main_area.winfo_children():
            widget.destroy()
        tk.Label(main_area, text="Contas de Utilizador", font=("Consolas", 18, "bold"), bg="white").pack(pady=10)
        tk.Button(main_area, text="Criar novo utilizador", font=("Consolas", 12), command=lambda: criar_utilizador(main_area)).pack(pady=10)

    def criar_utilizador(parent_frame):
        win = tk.Toplevel(def_win)
        win.title("Criar Utilizador")
        win.geometry("350x250+900+300")
        win.config(bg="white")

        tk.Label(win, text="Novo utilizador:", font=("Consolas", 14), bg="white").pack(pady=10)
        new_user = tk.Entry(win, font=("Consolas", 14))
        new_user.pack(pady=5)

        tk.Label(win, text="Password:", font=("Consolas", 14), bg="white").pack()
        new_pw = tk.Entry(win, font=("Consolas", 14), show="*")
        new_pw.pack(pady=5)

        is_admin = tk.BooleanVar()
        tk.Checkbutton(win, text="Administrador", variable=is_admin, bg="white", font=("Consolas", 12)).pack()

        def criar():
            users = load_users()
            u = new_user.get().strip()
            p = new_pw.get()
            if not u or not p:
                tk.messagebox.showerror("Erro", "Preencha todos os campos!", parent=win)
                return
            if u in users:
                tk.messagebox.showerror("Erro", "Utilizador já existe!", parent=win)
                return
            users[u] = {"password": hash_password(p), "admin": is_admin.get()}
            save_users(users)
            tk.messagebox.showinfo("Sucesso", "Utilizador criado!", parent=win)
            win.destroy()

        tk.Button(win, text="Criar", font=("Consolas", 14), command=criar).pack(pady=10)

    # Menu lateral
    btn_base = tk.Button(sidebar, text="Base", font=("Consolas", 13), bg="#eaf6ea", relief="flat", command=show_base)
    btn_base.pack(fill="x", pady=2)
    btn_users = tk.Button(sidebar, text="Contas", font=("Consolas", 13), bg="#eaf6ea", relief="flat", command=show_users)
    btn_users.pack(fill="x", pady=2)
    btn_close = tk.Button(sidebar, text="Fechar", font=("Consolas", 13), bg="#eaf6ea", relief="flat", command=def_win.destroy)
    btn_close.pack(fill="x", pady=20, side="bottom")

    # Mostra a secção "Base" por defeito
    show_base()