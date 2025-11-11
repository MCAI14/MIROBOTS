import tkinter as tk

def open_jogos(janela):
    # Remove todos os widgets atuais da janela
    for widget in janela.winfo_children():
        widget.destroy()
    
    # Cria o frame principal para a interface de Jogos
    jogos_frame = tk.Frame(janela, bg="blue")
    jogos_frame.pack(expand=True, fill="both")
    
    # Cria uma barra de título personalizada na parte superior
    title_bar = tk.Frame(jogos_frame, bg="darkblue", padx=5, pady=5)
    title_bar.pack(fill="x")
    
    # Label de título na barra (lado esquerdo)
    title_label = tk.Label(title_bar, text="Área de Jogos", 
                           font=("Consolas", 28), bg="darkblue", fg="white")
    title_label.pack(side="left")
    
    # Botão "X" para voltar ao desktop (lado direito) – integrado à barra de título
    voltar_btn = tk.Button(title_bar, text="X", 
                           font=("Consolas", 16), bg="lightgray", fg="black",
                           command=lambda: voltar(janela))
    voltar_btn.pack(side="right")
    
    # Cria um frame para os botões que ficarão abaixo da barra de título
    content_frame = tk.Frame(jogos_frame, bg="blue")
    content_frame.pack(expand=True, fill="both")
    
    # Botão "Jogos Offline"
    offline_btn = tk.Button(content_frame, text="Jogos Offline", 
                            font=("Consolas", 16), bg="lightgray", fg="black",
                            command=lambda: jogos_offline(janela))
    offline_btn.pack(pady=10)
    
    # Botão "Jogos Multiplayer (Necessita de Wi‑Fi)"
    multiplayer_btn = tk.Button(content_frame, 
                                 text="Jogos Online Multiplayer (Necessita de Wi‑Fi)", 
                                 font=("Consolas", 16), bg="lightgray", fg="black",
                                 command=lambda: jogos_multiplayer(janela))
    multiplayer_btn.pack(pady=10)

def voltar(janela):
    from users.guest import welcome
    welcome.open_desktop(janela)

def jogos_offline(janela):
    try:
        from users.guest.Programas.Jogos import OfflineGames
        OfflineGames.open_offline_games(janela)
    except Exception as e:
        print("Erro ao abrir Jogos Offline:", e)

def jogos_multiplayer(janela):
    try:
        from users.guest.Programas.Jogos import OnlineGames
        OnlineGames.open_online_games(janela)
    except Exception as e:
        print("Erro ao abrir Jogos Multiplayer:", e)