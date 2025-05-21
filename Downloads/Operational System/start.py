import tkinter as tk
import os
import json
import hashlib

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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

def open_user_selection(janela, splash):
    # Remove a tela de inicialização
    splash.destroy()
    users = load_users()

    # Cria um novo frame para a escolha de utilizadores
    user_selection_frame = tk.Frame(janela, bg="lightblue")
    user_selection_frame.pack(expand=True, fill="both")
    
    # Adiciona um Label simples com a mensagem para seleção
    label = tk.Label(user_selection_frame, text="Selecione o utilizador", font=("Consolas", 24), bg="lightblue", fg="black")
    label.pack(pady=20)
    
    user_var = tk.StringVar(value=list(users.keys())[0])
    user_menu = tk.OptionMenu(user_selection_frame, user_var, *users.keys())
    user_menu.config(font=("Consolas", 16))
    user_menu.pack(pady=10)

    password_label = tk.Label(user_selection_frame, text="Password:", font=("Consolas", 16), bg="lightblue")
    password_label.pack()
    password_entry = tk.Entry(user_selection_frame, font=("Consolas", 16), show="*")
    password_entry.pack(pady=5)

    def login():
        user = user_var.get()
        pw = password_entry.get()
        if users[user]["password"] == "" or users[user]["password"] == hash_password(pw):
            user_selection_frame.destroy()
            # Aqui podes passar o nome do utilizador para o ambiente de trabalho
            from users.guest.welcome import open_desktop
            open_desktop(janela)
        else:
            tk.messagebox.showerror("Erro", "Password incorreta!", parent=user_selection_frame)

    login_btn = tk.Button(user_selection_frame, text="Entrar", font=("Consolas", 16), command=login)
    login_btn.pack(pady=10)

    def open_create_user():
        create_win = tk.Toplevel(janela)
        create_win.title("Criar Utilizador")
        create_win.geometry("350x250+900+300")
        create_win.config(bg="white")

        tk.Label(create_win, text="Novo utilizador:", font=("Consolas", 14), bg="white").pack(pady=10)
        new_user = tk.Entry(create_win, font=("Consolas", 14))
        new_user.pack(pady=5)

        tk.Label(create_win, text="Password:", font=("Consolas", 14), bg="white").pack()
        new_pw = tk.Entry(create_win, font=("Consolas", 14), show="*")
        new_pw.pack(pady=5)

        is_admin = tk.BooleanVar()
        tk.Checkbutton(create_win, text="Administrador", variable=is_admin, bg="white", font=("Consolas", 12)).pack()

        def criar():
            u = new_user.get().strip()
            p = new_pw.get()
            if not u or not p:
                tk.messagebox.showerror("Erro", "Preencha todos os campos!", parent=create_win)
                return
            if u in users:
                tk.messagebox.showerror("Erro", "Utilizador já existe!", parent=create_win)
                return
            users[u] = {"password": hash_password(p), "admin": is_admin.get()}
            save_users(users)
            user_menu["menu"].add_command(label=u, command=tk._setit(user_var, u))
            tk.messagebox.showinfo("Sucesso", "Utilizador criado!", parent=create_win)
            create_win.destroy()

        tk.Button(create_win, text="Criar", font=("Consolas", 14), command=criar).pack(pady=10)

    tk.Button(user_selection_frame, text="Criar novo utilizador", font=("Consolas", 12), command=open_create_user).pack(pady=5)

    # Opções de energia
    def open_power_options():
        power_win = tk.Toplevel(janela)
        power_win.title("Opções de Energia")
        icon_path = os.path.join(ICONES_DIR, "Ligar-Desligar.png")
        try:
            icon_img = tk.PhotoImage(file=icon_path)
            power_win.iconphoto(True, icon_img)
            power_win._icon_img = icon_img
        except Exception as e:
            print("Erro ao definir o ícone de energia:", e)

        power_win.geometry("320x180+900+300")
        power_win.config(bg="white")

        label = tk.Label(power_win, text="O que pretende fazer?", font=("Consolas", 16, "bold"), bg="white")
        label.pack(pady=(20, 10))

        btn_frame = tk.Frame(power_win, bg="white")
        btn_frame.pack(pady=10)

        def encerrar():
            power_win.destroy()
            os.system("shutdown /s /t 0")

        def reiniciar():
            power_win.destroy()
            os.system("shutdown /r /t 0")

        def suspender():
            power_win.destroy()
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        tk.Button(btn_frame, text="Encerrar", font=("Consolas", 12), width=10, command=encerrar, bg="#ff5555", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Reiniciar", font=("Consolas", 12), width=10, command=reiniciar, bg="#ffaa00", fg="white").grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Suspender", font=("Consolas", 12), width=10, command=suspender, bg="#55aaff", fg="white").grid(row=0, column=2, padx=10)
        tk.Button(power_win, text="Cancelar", font=("Consolas", 12), width=10, command=power_win.destroy).pack(pady=10)

    # Frame para o botão de energia no canto inferior esquerdo
    power_frame = tk.Frame(user_selection_frame, bg="lightblue")
    power_frame.pack(side="left", anchor="sw", padx=10, pady=10, fill="y")

    btn_power = tk.Button(
        power_frame,
        text="Opções de Energia",
        font=("Consolas", 12),
        command=open_power_options
    )
    btn_power.pack(side="bottom", anchor="sw")