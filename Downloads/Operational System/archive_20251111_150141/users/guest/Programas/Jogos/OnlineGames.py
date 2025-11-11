import tkinter as tk

def open_online_games(janela):
    # Remove todos os widgets atuais da janela
    for widget in janela.winfo_children():
        widget.destroy()
    
    frame = tk.Frame(janela, bg="purple")
    frame.pack(expand=True, fill="both")
    
    label = tk.Label(frame, text="Jogos Online Multiplayer", font=("Consolas", 28), bg="purple", fg="white")
    label.pack(pady=20)
    
    # Adicione outros widgets e lógica conforme necessário.