from pathlib import Path

from src.facade import MimirFacade


PASTA_PDFS = Path(r"D:\Documentos\RPG\D&D")


def construir_indice():
    mimir = MimirFacade()
    caminho_indice = mimir.indexar_base(PASTA_PDFS)
    print(f"Índice salvo em: {caminho_indice}")


if __name__ == "__main__":
    construir_indice()
    