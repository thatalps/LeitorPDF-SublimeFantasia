# 🖨️ Leitor PDF com Impressão Automática de Imagens

Este projeto é uma aplicação desktop local desenvolvida em Python que lê o conteúdo de um arquivo PDF, identifica palavras-chave definidas em um arquivo JSON e, com base nelas, gera impressões automáticas de imagens correspondentes.

O sistema possui uma interface básica (Tkinter + CustomTkinter) e permite escolher a impressora, ajusta o tamanho das imagens para folha A4, imprime na horizontal, e até verifica atualizações automáticas via GitHub.

OBS.: Foi feito sob medida para a produção da loja Sublime Fantasia Artesanatos LTDA.

## Para gerar um executável com o PyInstaller é necessário rodar o trecho de código abaixo:
    pip install -r requirements.txt
    pip install pyinstaller
    pyinstaller --onefile --noconsole --add-data "data;data" src/main.py


