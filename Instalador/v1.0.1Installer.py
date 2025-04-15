import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário de traduções
translations = {
    "Português": {
        "welcome_title": "Bem-vindo ao MIROBOTS",
        "welcome_msg": "Este assistente irá guiá-lo pela instalação do MIROBOTS.",
        "config_title": "Configuração Inicial",
        "config_msg": "Selecione as configurações iniciais, como idioma, fuso horário e opções avançadas.",
        "language_label": "Idioma:",
        "auto_start_label": "Iniciar automaticamente o MIROBOTS ao ligar o computador:",
        "auto_start_yes": "Sim",
        "auto_start_no": "Não",
        "capacity_title": "Verificação de Capacidade",
        "capacity_msg": "Verificando se o seu computador possui os requisitos necessários...",
        "capacity_checking": "Verificando...",
        "capacity_failed": "Seu computador não possui a capacidade necessária.",
        "capacity_ok": "Seu computador está apto para rodar o MIROBOTS.",
        "review_title": "Revisão da Instalação",
        "review_msg": "Revise as configurações selecionadas antes de iniciar a instalação.",
        "installing": "Iniciando a instalação do MIROBOTS no idioma {language}...\nAuto Início: {auto}",
        "check_btn": "Iniciar Verificação",
        "details_title": "Detalhes da Verificação",
        "details_msg": "O sistema irá verificar os seguintes requisitos:\n- Processador\n- Memória RAM\n- Espaço em Disco\n- Placa Gráfica"
    },
    "Inglês": {
        "welcome_title": "Welcome to MIROBOTS",
        "welcome_msg": "This wizard will guide you through the MIROBOTS installation.",
        "config_title": "Initial Configuration",
        "config_msg": "Select initial configurations including language, time zone, and advanced options.",
        "language_label": "Language:",
        "auto_start_label": "Launch MIROBOTS automatically on startup:",
        "auto_start_yes": "Yes",
        "auto_start_no": "No",
        "capacity_title": "System Capacity Check",
        "capacity_msg": "Checking if your computer meets the necessary requirements...",
        "capacity_checking": "Checking...",
        "capacity_failed": "Your computer does not meet the required specifications.",
        "capacity_ok": "Your computer is capable of running MIROBOTS.",
        "review_title": "Installation Review",
        "review_msg": "Review the selected configurations before starting the installation.",
        "installing": "Starting MIROBOTS installation in {language}...\nAuto Launch: {auto}",
        "check_btn": "Start Check",
        "details_title": "Verification Details",
        "details_msg": "The system will check the following requirements:\n- Processor\n- RAM\n- Disk Space\n- Graphics Card"
    }
}


class InstallerWizard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assistente de Instalação MIROBOTS")
        self.geometry("600x400")
        # Estado inicial
        self.current_step = 0
        self.language = "Português"  # idioma padrão
        self.auto_start = translations[self.language]["auto_start_yes"]  # valor padrão: sim
        self.capacity_result = None  # resultado da verificação de capacidade
        self.steps = []
        self.create_steps()
        self.show_step(self.current_step)

    def create_steps(self):
        # Limpa passos anteriores (caso esteja reconstruindo após alteração de idioma)
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame) and widget not in [self]:
                widget.destroy()
        self.steps = []
        lang = translations[self.language]

        # Passo 1: Boas-vindas
        frame1 = ttk.Frame(self)
        ttk.Label(frame1, text=lang["welcome_title"], font=("Arial", 16)).pack(pady=20)
        ttk.Label(frame1, text=lang["welcome_msg"]).pack(pady=10)
        self.steps.append(frame1)

        # Passo 2: Configuração Inicial
        frame2 = ttk.Frame(self)
        ttk.Label(frame2, text=lang["config_title"], font=("Arial", 16)).pack(pady=20)
        ttk.Label(frame2, text=lang["config_msg"]).pack(pady=10)
        # Seleção de idioma
        ttk.Label(frame2, text=lang["language_label"]).pack(pady=(10,0))
        self.idioma_cb = ttk.Combobox(frame2, values=["Português", "Inglês", "Espanhol"])
        self.idioma_cb.set(self.language)
        self.idioma_cb.pack(pady=5)
        self.idioma_cb.bind("<<ComboboxSelected>>", self.change_language)
        # Opção de Auto-início
        ttk.Label(frame2, text=lang["auto_start_label"]).pack(pady=(10,0))
        self.auto_var = tk.StringVar(value=lang["auto_start_yes"])
        rb1 = ttk.Radiobutton(frame2, text=lang["auto_start_yes"], variable=self.auto_var, value=lang["auto_start_yes"])
        rb2 = ttk.Radiobutton(frame2, text=lang["auto_start_no"], variable=self.auto_var, value=lang["auto_start_no"])
        rb1.pack(pady=2)
        rb2.pack(pady=2)
        self.steps.append(frame2)

        # Passo 3: Detalhes da Verificação
        frame3 = ttk.Frame(self)
        ttk.Label(frame3, text=lang["details_title"], font=("Arial", 16)).pack(pady=20)
        ttk.Label(frame3, text=lang["details_msg"]).pack(pady=10)
        self.steps.append(frame3)

        # Passo 4: Verificação de Capacidade (inicia automaticamente)
        frame4 = ttk.Frame(self)
        ttk.Label(frame4, text=lang["capacity_title"], font=("Arial", 16)).pack(pady=20)
        self.capacity_label = ttk.Label(frame4, text=lang["capacity_msg"])
        self.capacity_label.pack(pady=10)
        # Aqui não incluímos o botão "Start Check"
        self.steps.append(frame4)

        # Passo 5: Revisão da Instalação
        frame5 = ttk.Frame(self)
        ttk.Label(frame5, text=lang["review_title"], font=("Arial", 16)).pack(pady=20)
        self.review_text = ttk.Label(frame5, text="")
        self.review_text.pack(pady=10)
        self.steps.append(frame5)

    def change_language(self, event):
        # Atualiza o idioma e reconstrói os passos para refletir as mudanças
        self.language = self.idioma_cb.get()
        messagebox.showinfo("Idioma Alterado", f"Idioma alterado para: {self.language}")
        self.auto_var.set(translations[self.language]["auto_start_yes"])
        self.create_steps()
        self.show_step(self.current_step)

    def show_step(self, index):
        for step in self.steps:
            step.pack_forget()
        self.steps[index].pack(fill=tk.BOTH, expand=True)
        self.update_nav()
        if index == 3:
            # No Passo 4, inicia automaticamente a verificação de capacidade
            self.run_capacity_check()
        if index == len(self.steps) - 1:
            self.update_review()

    def update_nav(self):
        if hasattr(self, 'nav_frame'):
            self.nav_frame.destroy()

        self.nav_frame = ttk.Frame(self)
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        if self.current_step > 0:
            prev_btn = ttk.Button(self.nav_frame, text="Anterior", command=self.prev_step)
            prev_btn.pack(side=tk.LEFT, padx=20)

        # No Passo 3, exibe o botão "Iniciar Verificação" (em vez de "Próximo")
        if self.current_step == 2:
            start_btn = ttk.Button(self.nav_frame, text=translations[self.language]["check_btn"], command=self.start_verification)
            start_btn.pack(side=tk.RIGHT, padx=20)
            return

        # No Passo 4, exibe "Próximo" somente se a verificação foi concluída
        if self.current_step == 3:
            if self.capacity_result is not None:
                next_btn = ttk.Button(self.nav_frame, text="Próximo", command=self.next_step)
                next_btn.pack(side=tk.RIGHT, padx=20)
            return

        if self.current_step < len(self.steps) - 1:
            next_btn = ttk.Button(self.nav_frame, text="Próximo", command=self.next_step)
            next_btn.pack(side=tk.RIGHT, padx=20)
        else:
            install_btn = ttk.Button(self.nav_frame, text="Instalar", command=self.install)
            install_btn.pack(side=tk.RIGHT, padx=20)

    def start_verification(self):
        # Avança para o Passo 4 e inicia a verificação automaticamente
        self.current_step += 1
        self.show_step(self.current_step)

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_step(self.current_step)

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step(self.current_step)

    def run_capacity_check(self):
        lang = translations[self.language]
        self.capacity_label.config(text=lang["capacity_checking"])
        self.update()
        # Simula a verificação com delay de 2 segundos
        self.after(2000, self.finish_capacity_check)

    def finish_capacity_check(self):
        self.capacity_result = True  # Simulação: capacidade OK
        lang = translations[self.language]
        if self.capacity_result:
            self.capacity_label.config(text=lang["capacity_ok"])
        else:
            self.capacity_label.config(text=lang["capacity_failed"])
        self.update_nav()

    def update_review(self):
        lang = translations[self.language]
        auto_choice = self.auto_var.get()
        review_msg = f"{lang['review_msg']}\n\nIdioma: {self.language}\n" \
                     f"{lang['auto_start_label']} {auto_choice}\n" \
                     f"{lang['capacity_title']}: "
        if self.capacity_result is None:
            review_msg += "Não verificado"
        elif self.capacity_result:
            review_msg += lang["capacity_ok"]
        else:
            review_msg += lang["capacity_failed"]
        self.review_text.config(text=review_msg)

    def install(self):
        lang = translations[self.language]
        auto_choice = self.auto_var.get()
        messagebox.showinfo("Instalação", lang["installing"].format(language=self.language, auto=auto_choice))
        messagebox.showinfo("Instalação", "MIROBOTS instalado com sucesso!")
        self.destroy()


if __name__ == "__main__":
    app = InstallerWizard()
    app.mainloop()