import tkinter as tk

def open_offline_games(janela):
    # Remove todos os widgets atuais da janela
    for widget in janela.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(janela, bg="green")
    frame.pack(expand=True, fill="both")
    
    label = tk.Label(frame, text="Jogos Offline", font=("Consolas", 28), bg="green", fg="white")
    label.pack(pady=20)
    
    # Adicione outros widgets e lógica conforme necessário.