import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

def open_codepode(parent):
    win = tk.Toplevel(parent)
    win.title("MIROBOTS CodePode")
    win.geometry("900x600+400+100")
    win.config(bg="white")

    # Ícone (opcional)
    icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "Operational System", "icones", "CodePode.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        win.iconphoto(True, icon_img)
        win._icon_img = icon_img
    except Exception:
        pass

    # Frame lateral para navegação de ficheiros
    sidebar = tk.Frame(win, width=200, bg="#222")
    sidebar.pack(side="left", fill="y")

    # Frame principal para as abas
    main = tk.Frame(win, bg="white")
    main.pack(side="right", expand=True, fill="both")

    # Lista de ficheiros
    file_list = tk.Listbox(sidebar, bg="#222", fg="white", font=("Consolas", 11))
    file_list.pack(expand=True, fill="both", padx=5, pady=5)

    # Abas
    notebook = ttk.Notebook(main)
    notebook.pack(expand=True, fill="both")

    # Função para abrir pasta
    def open_folder():
        folder = filedialog.askdirectory(parent=win)
        if folder:
            file_list.delete(0, tk.END)
            for root, dirs, files in os.walk(folder):
                for f in files:
                    path = os.path.relpath(os.path.join(root, f), folder)
                    file_list.insert(tk.END, path)
            win.folder = folder

    # Função para abrir ficheiro numa nova aba
    def open_file_in_tab(filename):
        for i in range(notebook.index("end")):
            if notebook.tab(i, "text") == filename:
                notebook.select(i)
                return
        try:
            with open(os.path.join(win.folder, filename), "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o ficheiro:\n{e}", parent=win)
            return
        frame = tk.Frame(notebook, bg="white")
        text = tk.Text(frame, font=("Consolas", 12), wrap="word")
        text.insert("1.0", content)
        text.pack(expand=True, fill="both")
        notebook.add(frame, text=filename)
        notebook.select(frame)

        # Botão para guardar
        def guardar():
            try:
                with open(os.path.join(win.folder, filename), "w", encoding="utf-8") as f:
                    f.write(text.get("1.0", tk.END))
                messagebox.showinfo("Guardado", "Ficheiro guardado com sucesso!", parent=win)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível guardar:\n{e}", parent=win)
        btn = tk.Button(frame, text="Guardar", command=guardar)
        btn.pack(anchor="ne", padx=5, pady=5)

    # Evento ao clicar num ficheiro
    def on_file_select(event):
        if hasattr(win, "folder"):
            sel = file_list.curselection()
            if sel:
                filename = file_list.get(sel[0])
                open_file_in_tab(filename)

    file_list.bind("<Double-Button-1>", on_file_select)

    # Botão para abrir pasta
    btn_folder = tk.Button(sidebar, text="Abrir Pasta", command=open_folder, bg="#444", fg="white")
    btn_folder.pack(fill="x", padx=5, pady=5)

    # Botão para fechar o CodePode
    btn_fechar = tk.Button(sidebar, text="Fechar", command=win.destroy, bg="#444", fg="white")
    btn_fechar.pack(fill="x", padx=5, pady=5)