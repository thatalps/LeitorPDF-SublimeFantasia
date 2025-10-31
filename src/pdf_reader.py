import fitz  # PyMuPDF
import json

def process_pdf(pdf_path):
    # Lê o texto do PDF
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    print(text)
    doc.close()

    # Lê o JSON
    with open("data/keywords.json", "r", encoding="utf-8") as f:
        keywords = json.load(f)

    counts = {}
    for keyword, images in keywords.items():
        keyword = keyword
        # Normaliza: transforma string em lista, se necessário
        if isinstance(images, str):
            images = [images]

        qtd = text.count(keyword)
        counts[keyword] = (images, qtd)
    return counts
