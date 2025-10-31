import fitz, json, re
from utils import resource_path

def process_pdf(pdf_path):
    # Lê o texto do PDF
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    doc.close()
    #Remove quebra de linha e espaçamento
    text = text.replace('\n', '')
    text = re.sub(r'\s+', '', text)

    # Lê o JSON
    json_path = resource_path("data/keywords.json")
    with open(json_path, "r", encoding="utf-8") as f:
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
