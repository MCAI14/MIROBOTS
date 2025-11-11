import tkinter as tk
import os
from tkinter import filedialog, messagebox

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ICONES_DIR = os.path.join(BASE_DIR, "Operational System", "icones")

def open_editor_texto(parent):
    editor_win = tk.Toplevel(parent)
    editor_win.title("Editor de Texto")
    editor_win.transient(None)
    editor_win.attributes("-toolwindow", False)
    icon_path = os.path.join(ICONES_DIR, "EditorTexto.png")
    try:
        icon_img = tk.PhotoImage(file=icon_path)
        editor_win.iconphoto(True, icon_img)
        editor_win._icon_img = icon_img
    except Exception as e:
        print("Erro ao definir o ícone do editor de texto:", e)

    editor_win.geometry("600x400+800+200")
    editor_win.config(bg="white")

    text_area = tk.Text(editor_win, font=("Consolas", 12), wrap="word")
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    # Variável para controlar se o texto foi guardado
    texto_guardado = {"valor": True}
    texto_atual = {"conteudo": ""}

    def marcar_modificado(event=None):
        texto_guardado["valor"] = False

    text_area.bind("<<Modified>>", marcar_modificado)

    def guardar():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Ficheiros de Texto", "*.txt")],
            parent=editor_win
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text_area.get("1.0", tk.END))
                messagebox.showinfo("Sucesso", "Ficheiro guardado com sucesso!", parent=editor_win)
                texto_guardado["valor"] = True
                texto_atual["conteudo"] = text_area.get("1.0", tk.END)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível guardar: {e}", parent=editor_win)

    def abrir():
        file_path = filedialog.askopenfilename(
            filetypes=[("Ficheiros de Texto", "*.txt")],
            parent=editor_win
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text_area.delete("1.0", tk.END)
                    text_area.insert(tk.END, f.read())
                texto_guardado["valor"] = True
                texto_atual["conteudo"] = text_area.get("1.0", tk.END)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir: {e}", parent=editor_win)

    def fechar():
        if not texto_guardado["valor"] and text_area.get("1.0", tk.END) != texto_atual["conteudo"]:
            resposta = messagebox.askyesnocancel(
                "Aviso",
                "Tem alterações não guardadas. Deseja guardar antes de sair?",
                parent=editor_win
            )
            if resposta is None:
                return  # Cancelar o fecho
            elif resposta:
                guardar()
                if texto_guardado["valor"]:
                    editor_win.destroy()
            else:
                # Não guardar, fecha o editor
                editor_win.destroy()
        else:
            editor_win.destroy()

    btn_frame = tk.Frame(editor_win, bg="white")
    btn_frame.pack(fill="x", padx=10, pady=5)

    btn_abrir = tk.Button(btn_frame, text="Abrir", command=abrir)
    btn_abrir.pack(side="left", padx=5)
    btn_guardar = tk.Button(btn_frame, text="Guardar", command=guardar)
    btn_guardar.pack(side="left", padx=5)
    btn_fechar = tk.Button(btn_frame, text="Fechar", command=fechar)
    btn_fechar.pack(side="right", padx=5)

    # Intercepta o fecho da janela pelo X
    editor_win.protocol("WM_DELETE_WINDOW", fechar)