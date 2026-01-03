import os
import shutil
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox


class BotOrganizador:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Organizador de Arquivos")
        self.root.geometry("520x360")
        ctk.set_appearance_mode("dark")

        self.caminho_selecionado: Path | None = None

        # Pastas do sistema (bloqueio real, por path absoluto)
        self.pastas_proibidas = [
            Path("C:/Windows"),
            Path("C:/Program Files"),
            Path("C:/Program Files (x86)"),
            Path("C:/Users").joinpath(os.getlogin(), "AppData")
        ]

        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(
            self.root,
            text="Organizador Automático de Arquivos",
            font=("Arial", 20, "bold")
        )
        self.label.pack(pady=20)

        self.btn_selecionar = ctk.CTkButton(
            self.root,
            text="Selecionar Pasta",
            command=self.selecionar_pasta
        )
        self.btn_selecionar.pack(pady=10)

        self.caminho_label = ctk.CTkLabel(
            self.root,
            text="Nenhuma pasta selecionada",
            wraplength=450
        )
        self.caminho_label.pack(pady=10)

        self.btn_executar = ctk.CTkButton(
            self.root,
            text="Organizar Agora",
            fg_color="green",
            hover_color="darkgreen",
            state="disabled",
            command=self.organizar_arquivos
        )
        self.btn_executar.pack(pady=20)

    def selecionar_pasta(self):
        caminho = filedialog.askdirectory()
        if not caminho:
            return

        caminho = Path(caminho).resolve()

        if self.pasta_proibida(caminho):
            messagebox.showerror(
                "Erro de Segurança",
                "Esta pasta é protegida e não pode ser organizada."
            )
            return

        self.caminho_selecionado = caminho
        self.caminho_label.configure(text=f"Pasta: {caminho}")
        self.btn_executar.configure(state="normal")

    def pasta_proibida(self, caminho: Path) -> bool:
        return any(caminho.is_relative_to(p) for p in self.pastas_proibidas if p.exists())

    def organizar_arquivos(self):
        if not self.caminho_selecionado:
            return

        pasta = self.caminho_selecionado
        arquivos_movidos = 0
        erros = 0

        for item in pasta.iterdir():
            if not item.is_file():
                continue

            extensao = item.suffix.lower().replace(".", "")
            if not extensao:
                extensao = "outros"

            destino = pasta / extensao.upper()
            destino.mkdir(exist_ok=True)

            try:
                shutil.move(str(item), destino / item.name)
                arquivos_movidos += 1
            except Exception:
                erros += 1

        messagebox.showinfo(
            "Finalizado",
            f"Arquivos movidos: {arquivos_movidos}\nErros: {erros}"
        )


if __name__ == "__main__":
    app = ctk.CTk()
    BotOrganizador(app)
    app.mainloop()
