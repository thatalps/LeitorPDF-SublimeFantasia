import customtkinter as ctk
from printer_config import PrinterConfig
from tkinter import filedialog, messagebox
from pdf_reader import process_pdf
from printer import print_image
from sync import check_updates, pull_updates
import os, sys

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Leitor PDF - Impressão Automática")
        self.geometry("600x400")

        # Configurações da impressora
        self.printer_config = PrinterConfig(self)

        self.label = ctk.CTkLabel(self, text="Selecione um PDF para processar", font=("Arial", 16))
        self.label.pack(pady=50)

        # Botões principais
        self.btn_open = ctk.CTkButton(self, text="📂 Inserir PDF", font=("Arial", 16), command=self.open_pdf)
        self.btn_open.pack(pady=10)

        self.btn_check_updates = ctk.CTkButton(self, text="🔄 Verificar atualizações", command=self.verify_updates)
        self.btn_check_updates.pack(pady=30)

    def open_pdf(self):

        # 1️⃣ Abre a janela para selecionar o PDF
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not pdf_path:
            return  # sai se nenhum arquivo foi selecionado

        try:
            # 2️⃣ Processa o PDF e retorna um dicionário: {palavra: (lista_de_imagens, qtd)}
            counts = process_pdf(pdf_path)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao processar o PDF:\n{e}")
            return

        total_imgs = 0  # contador de imagens impressas

        # 3️⃣ Percorre cada palavra-chave encontrada
        for keyword, (image_list, qtd) in counts.items():
            if qtd == 0:
                continue  # pula palavras não encontradas

            # 4️⃣ Para cada ocorrência da palavra, imprime todas as imagens associadas
            for _ in range(qtd):
                for image_path in image_list:
                    try:
                        print_image(
                            image_path,
                            printer_name=self.printer_config.selected_printer.get(),
                            fit_a4=self.printer_config.fit_a4.get(),
                            horizontal=self.printer_config.horizontal.get()
                        )
                        total_imgs += 1
                    except Exception as e:
                        print(f"Erro ao imprimir {image_path}: {e}")

        # 5️⃣ Exibe mensagem final com total de imagens impressas
        messagebox.showinfo("Concluído", f"Impressão concluída!\nTotal de imagens: {total_imgs}")



    def verify_updates(self):
        repo_path = os.getcwd()
        try:
            if check_updates(repo_path):
                resposta = messagebox.askyesno("Atualização disponível", "Nova versão disponível!\n\nDeseja atualizar e reiniciar agora?")
                if resposta:
                    self.update_and_restart()
            else:
                messagebox.showinfo("Atualização", "Nenhuma atualização encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao verificar atualizações:\n{e}")
    def update_and_restart(self):
        repo_path = os.getcwd()
        try:
            pull_updates(repo_path)
            messagebox.showinfo("Atualização", "Aplicação atualizada com sucesso!\nReiniciando...")
            os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar:\n{e}")
if __name__ == "__main__":
    app = App()
    app.mainloop()
