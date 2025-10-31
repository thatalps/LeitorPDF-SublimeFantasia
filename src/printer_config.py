import win32print
import customtkinter as ctk

class PrinterConfig:
    def __init__(self, master):
        # Lista de impressoras disponíveis
        self.printers = [printer[2] for printer in win32print.EnumPrinters(2)]
        self.selected_printer = ctk.StringVar(value=win32print.GetDefaultPrinter())

        # Configurações adicionais
        self.fit_a4 = ctk.BooleanVar(value=True)
        self.horizontal = ctk.BooleanVar(value=True)

        # Widgets (dropdown de impressoras)
        self.label_printer = ctk.CTkLabel(master, text="Selecione a impressora:", font=("Arial", 12))
        self.label_printer.pack(pady=5)

        self.dropdown_printers = ctk.CTkOptionMenu(master, variable=self.selected_printer, values=self.printers)
        self.dropdown_printers.pack(pady=5)
