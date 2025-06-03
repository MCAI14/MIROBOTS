import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

def open_codepode(parent):
    win = tk.Toplevel(parent)
    win.title("CodePode")
    win.geometry("1000x650+300+100")
    win.config(bg="#23272e")

    # Ícone (opcional)
    icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "Operational System", "icones", "CodePode.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        win.iconphoto(True, icon_img)
        win._icon_img = icon_img
    except Exception:
        pass

    # Barra superior customizada
    topbar = tk.Frame(win, bg="#181c22", height=40)
    topbar.pack(side="top", fill="x")

    # Botões com ícones (usa PNGs ou emojis se não tiveres imagens)
    def get_icon(name, fallback):
        try:
            return tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "..", "..", "..", "Operational System", "icones", name))
        except Exception:
            return None

    open_icon = get_icon("abrir.png", "📂")
    save_icon = get_icon("guardar.png", "💾")
    close_icon = get_icon("fechar.png", "❌")

    btn_open = tk.Button(topbar, image=open_icon, text=" Abrir", compound="left", font=("Consolas", 11), bg="#23272e", fg="white", bd=0, command=lambda: open_folder())
    btn_open.image = open_icon
    btn_open.pack(side="left", padx=8, pady=4)

    btn_save = tk.Button(topbar, image=save_icon, text=" Guardar", compound="left", font=("Consolas", 11), bg="#23272e", fg="white", bd=0, command=lambda: save_current())
    btn_save.image = save_icon
    btn_save.pack(side="left", padx=8, pady=4)

    btn_close = tk.Button(topbar, image=close_icon, text=" Fechar aba", compound="left", font=("Consolas", 11), bg="#23272e", fg="white", bd=0, command=lambda: close_tab())
    btn_close.image = close_icon
    btn_close.pack(side="left", padx=8, pady=4)

    # Frame lateral para navegação de ficheiros
    sidebar = tk.Frame(win, width=220, bg="#181c22")
    sidebar.pack(side="left", fill="y")

    # Lista de ficheiros
    file_list = tk.Listbox(sidebar, bg="#23272e", fg="#b6b6b6", font=("Consolas", 11), selectbackground="#3b4252", borderwidth=0, highlightthickness=0)
    file_list.pack(expand=True, fill="both", padx=0, pady=0)

    # Frame principal para as abas
    main = tk.Frame(win, bg="#23272e")
    main.pack(side="right", expand=True, fill="both")

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TNotebook", background="#23272e", borderwidth=0)
    style.configure("TNotebook.Tab", background="#23272e", foreground="#b6b6b6", font=("Consolas", 11), padding=[12, 6])
    style.map("TNotebook.Tab", background=[("selected", "#3b4252")], foreground=[("selected", "#fff")])

    notebook = ttk.Notebook(main, style="TNotebook")
    notebook.pack(expand=True, fill="both")

    win.folder = None
    open_tabs = {}

    def open_folder():
        folder = filedialog.askdirectory(parent=win)
        if folder:
            file_list.delete(0, tk.END)
            for root, dirs, files in os.walk(folder):
                for f in files:
                    path = os.path.relpath(os.path.join(root, f), folder)
                    file_list.insert(tk.END, path)
            win.folder = folder

    def open_file_in_tab(filename):
        if filename in open_tabs:
            notebook.select(open_tabs[filename])
            return
        try:
            with open(os.path.join(win.folder, filename), "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o ficheiro:\n{e}", parent=win)
            return
        frame = tk.Frame(notebook, bg="#23272e")
        text = tk.Text(frame, font=("Consolas", 13), wrap="none", bg="#23272e", fg="#eaeaea", insertbackground="#fff", borderwidth=0, highlightthickness=0, selectbackground="#3b4252")
        text.insert("1.0", content)
        text.pack(expand=True, fill="both", padx=0, pady=0)
        notebook.add(frame, text=filename)
        notebook.select(frame)
        open_tabs[filename] = frame

        # Destaque da linha atual
        def highlight_line(event=None):
            text.tag_remove("active_line", "1.0", "end")
            text.tag_add("active_line", "insert linestart", "insert lineend+1c")
            text.tag_configure("active_line", background="#2c313c")
        text.bind("<KeyRelease>", highlight_line)
        text.bind("<ButtonRelease>", highlight_line)
        highlight_line()

        # Guardar ficheiro
        def guardar():
            try:
                with open(os.path.join(win.folder, filename), "w", encoding="utf-8") as f:
                    f.write(text.get("1.0", tk.END))
                messagebox.showinfo("Guardado", "Ficheiro guardado com sucesso!", parent=win)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível guardar:\n{e}", parent=win)

        # Adiciona botão de guardar na própria aba (opcional)
        btn = tk.Button(frame, text="Guardar", command=guardar, bg="#3b4252", fg="#fff", font=("Consolas", 10), bd=0)
        btn.pack(anchor="ne", padx=8, pady=8)

    def on_file_select(event):
        if hasattr(win, "folder"):
            sel = file_list.curselection()
            if sel:
                filename = file_list.get(sel[0])
                open_file_in_tab(filename)

    file_list.bind("<Double-Button-1>", on_file_select)

    def save_current():
        idx = notebook.index("current")
        if idx is not None:
            frame = notebook.nametowidget(notebook.tabs()[idx])
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Text):
                    filename = notebook.tab(idx, "text")
                    try:
                        with open(os.path.join(win.folder, filename), "w", encoding="utf-8") as f:
                            f.write(widget.get("1.0", tk.END))
                        messagebox.showinfo("Guardado", "Ficheiro guardado com sucesso!", parent=win)
                    except Exception as e:
                        messagebox.showerror("Erro", f"Não foi possível guardar:\n{e}", parent=win)

    def close_tab():
        idx = notebook.index("current")
        if idx is not None:
            filename = notebook.tab(idx, "text")
            notebook.forget(idx)
            if filename in open_tabs:
                del open_tabs[filename]

    # Botão para abrir pasta na sidebar
    btn_folder = tk.Button(sidebar, text="📂 Abrir Pasta", command=open_folder, bg="#181c22", fg="#fff", font=("Consolas", 11), bd=0)
    btn_folder.pack(fill="x", padx=8, pady=8)

    # Botão para fechar o CodePode
    btn_fechar = tk.Button(sidebar, text="❌ Fechar", command=win.destroy, bg="#181c22", fg="#fff", font=("Consolas", 11), bd=0)
    btn_fechar.pack(fill="x", padx=8, pady=8)