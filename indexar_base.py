from pathlib import Path

from src.chunking import chunking
from src.embeddings import adicionar_embeddings
from src.loader import buscar_pdfs, ler_documentos
from src.vector_store import indexar_chunks

PASTA_PDFS = Path(r"D:\Documentos\RPG\D&D")

def construir_indice():
    arquivos = buscar_pdfs(PASTA_PDFS)
    print(f"PDFs encontrados: {len(arquivos)}")

    documentos = ler_documentos(arquivos)
    print(f"Páginas com texto: {len(documentos)}")

    chunks = chunking(documentos)
    print(f"Chunks criados: {len(chunks)}")

    chunks = adicionar_embeddings(chunks)
    print("Embeddings gerados.")

    caminho_indice = indexar_chunks(chunks)
    print(f"Índice salvo em: {caminho_indice}")

if __name__ == "__main__":
    construir_indice()
