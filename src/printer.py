import win32print, win32ui
from utils import resource_path
from PIL import Image, ImageWin
def print_image(image_path, printer_name, fit_a4=True, horizontal=True):
    try:
        # Ajusta o caminho da imagem
        full_path = resource_path(image_path)
        # Abre a imagem
        img = Image.open(image_path)

        # Ajuste para A4 horizontal se necessário
        if fit_a4:
            width = 3508  # 297mm em px @300dpi
            height = 2480  # 210mm em px @300dpi
            if not horizontal:
                width, height = height, width
            img = img.resize((width, height), Image.Resampling.LANCZOS)

        # Envia para impressora
        hprinter = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(hprinter, 2)
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc(image_path)
        hdc.StartPage()

        dib = ImageWin.Dib(img)
        dib.draw(hdc.GetHandleOutput(), (0, 0, width, height))

        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()
        win32print.ClosePrinter(hprinter)

    except Exception as e:
        print(f"Erro ao imprimir {image_path}: {e}")
