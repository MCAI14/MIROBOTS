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

    def_win.geometry("1100x650+300+100")
    def_win.config(bg="#f6fcf6")

    # --- Menu lateral ---
    sidebar = tk.Frame(def_win, bg="#eaf6ea", width=220)
    sidebar.pack(side="left", fill="y")

    # --- Área principal ---
    main_area = tk.Frame(def_win, bg="white")
    main_area.pack(side="right", expand=True, fill="both")

    # --- Perfil do utilizador ---
    profile_frame = tk.Frame(sidebar, bg="#eaf6ea")
    profile_frame.pack(fill="x", pady=(10, 0))

    # Imagem de perfil (placeholder)
    try:
        profile_img_path = os.path.join(ICONES_DIR, "user.png")
        profile_img = tk.PhotoImage(file=profile_img_path)
        profile_label = tk.Label(profile_frame, image=profile_img, bg="#eaf6ea")
        profile_label.image = profile_img
        profile_label.pack(pady=(0, 5))
    except Exception:
        profile_label = tk.Label(profile_frame, text="👤", font=("Arial", 32), bg="#eaf6ea")
        profile_label.pack(pady=(0, 5))

    tk.Label(profile_frame, text="Misha Inácio", font=("Consolas", 13, "bold"), bg="#eaf6ea").pack()
    tk.Label(profile_frame, text="misha14@outlook.pt", font=("Consolas", 10), bg="#eaf6ea", fg="#555").pack()

    # Caixa de pesquisa
    search_entry = tk.Entry(sidebar, font=("Consolas", 11), relief="flat")
    search_entry.insert(0, "Procurar uma definição")
    search_entry.pack(fill="x", padx=10, pady=10)

    # --- Botões do menu lateral ---
    menu_items = [
        ("Base", "🏠"),
        ("Sistema", "💻"),
        ("Bluetooth e dispositivos", "📶"),
        ("Rede e Internet", "🌐"),
        ("Personalização", "🎨"),
        ("Aplicações", "🗂️"),
        ("Contas", "👥"),
        ("Hora e idioma", "⏰"),
        ("Jogos", "🎮"),
        ("Acessibilidade", "🦽"),
        ("Privacidade e segurança", "🔒"),
        ("Windows Update", "🔄"),
    ]

    def clear_main():
        for widget in main_area.winfo_children():
            widget.destroy()

    def show_base():
        clear_main()
        tk.Label(main_area, text="Base", font=("Consolas", 22, "bold"), bg="white").pack(anchor="nw", padx=30, pady=(20, 0))
        # Simulação dos cartões e widgets principais
        cards_frame = tk.Frame(main_area, bg="white")
        cards_frame.pack(anchor="nw", padx=30, pady=20, fill="x")

        # Cartão do dispositivo
        device_card = tk.Frame(cards_frame, bg="#f8f8f8", bd=1, relief="solid")
        device_card.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
        tk.Label(device_card, text="WINDOWS-MI-11", font=("Consolas", 13, "bold"), bg="#f8f8f8").pack(padx=20, pady=(10, 0))
        tk.Label(device_card, text="20LAS4FB00", font=("Consolas", 10), bg="#f8f8f8").pack(padx=20)
        tk.Label(device_card, text="Mudar o Nome", font=("Consolas", 9, "underline"), fg="blue", bg="#f8f8f8", cursor="hand2").pack(padx=20, pady=(0, 10))

        # Cartão de definições recomendadas
        rec_card = tk.Frame(cards_frame, bg="#f8f8f8", bd=1, relief="solid")
        rec_card.grid(row=0, column=1, padx=10, pady=5, sticky="nw")
        tk.Label(rec_card, text="Definições recomendadas", font=("Consolas", 13, "bold"), bg="#f8f8f8").pack(padx=20, pady=(10, 0))
        tk.Label(rec_card, text="Definições recentes e vulgarmente utilizadas", font=("Consolas", 10), bg="#f8f8f8").pack(padx=20)
        tk.Label(rec_card, text="Som", font=("Consolas", 11), bg="#f8f8f8").pack(anchor="w", padx=20, pady=(5, 0))
        tk.Label(rec_card, text="Ecrã", font=("Consolas", 11), bg="#f8f8f8").pack(anchor="w", padx=20)
        tk.Label(rec_card, text="Impressoras e scanners", font=("Consolas", 11), bg="#f8f8f8").pack(anchor="w", padx=20, pady=(0, 10))

        # Cartão de armazenamento na nuvem
        cloud_card = tk.Frame(cards_frame, bg="#f8f8f8", bd=1, relief="solid")
        cloud_card.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        tk.Label(cloud_card, text="Armazenamento na nuvem", font=("Consolas", 13, "bold"), bg="#f8f8f8").pack(padx=20, pady=(10, 0))
        tk.Label(cloud_card, text="Parece que está a utilizar uma conta diferente no OneDrive.", font=("Consolas", 10), bg="#f8f8f8", wraplength=220, justify="left").pack(padx=20)
        tk.Button(cloud_card, text="Abrir contas do OneDrive", font=("Consolas", 10)).pack(padx=20, pady=(0, 10))

        # Cartão de dispositivos Bluetooth
        bt_card = tk.Frame(cards_frame, bg="#f8f8f8", bd=1, relief="solid")
        bt_card.grid(row=1, column=1, padx=10, pady=5, sticky="nw")
        tk.Label(bt_card, text="Dispositivos Bluetooth", font=("Consolas", 13, "bold"), bg="#f8f8f8").pack(padx=20, pady=(10, 0))
        tk.Label(bt_card, text="Bluetooth: Ligado", font=("Consolas", 10), bg="#f8f8f8").pack(anchor="w", padx=20)
        tk.Label(bt_card, text="Microsoft Bluetooth Mouse\nEmparelhado", font=("Consolas", 10), bg="#f8f8f8").pack(anchor="w", padx=20)
        tk.Label(bt_card, text="iS wireless keyboard\nEmparelhado", font=("Consolas", 10), bg="#f8f8f8").pack(anchor="w", padx=20, pady=(0, 10))

    def show_users():
        clear_main()
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

    # Criar botões do menu lateral dinamicamente
    btns = []
    for name, emoji in menu_items:
        if name == "Base":
            cmd = show_base
        elif name == "Contas":
            cmd = show_users
        else:
            cmd = lambda n=name: [clear_main(), tk.Label(main_area, text=n, font=("Consolas", 18, "bold"), bg="white").pack(pady=20)]
        btn = tk.Button(sidebar, text=f"{emoji}  {name}", font=("Consolas", 13), bg="#eaf6ea", relief="flat", anchor="w", command=cmd)
        btn.pack(fill="x", pady=1, padx=5)
        btns.append(btn)

    btn_close = tk.Button(sidebar, text="Fechar", font=("Consolas", 13), bg="#eaf6ea", relief="flat", command=def_win.destroy)
    btn_close.pack(fill="x", pady=20, side="bottom")

    # Mostra a secção "Base" por defeito
    show_base()