import sys, os

def resource_path(relative_path):
    """Obtém o caminho absoluto do recurso, compatível com PyInstaller."""
    try:
        # Quando executado pelo PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Quando executado pelo código fonte
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

