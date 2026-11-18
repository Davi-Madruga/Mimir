from pathlib import Path
from pypdf import PdfReader


def buscar_pdfs(pasta):
    pasta = Path(pasta)

    if not pasta.is_dir():
        raise NotADirectoryError(f"Pasta não encontrada: {pasta}")

    return sorted(pasta.rglob("*.pdf"))


def ler_documentos(arquivos):
    documentos = []

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")

        leitor = PdfReader(arquivo)

        for numero, pagina in enumerate(leitor.pages, start=1):
            texto = pagina.extract_text() or ""

            if not texto.strip():
                continue

            documento = {
                "arquivo": arquivo.name,
                "caminho": str(arquivo),
                "pagina": numero,
                "texto": texto,
            }

            documentos.append(documento)

    return documentos


if __name__ == "__main__":
    pasta = Path(r"D:\Documentos\RPG\D&D")

    arquivos = buscar_pdfs(pasta)
    print(f"PDFs encontrados: {len(arquivos)}")
    for arquivo in arquivos:
        print(arquivo.name)

    documentos = ler_documentos(arquivos)

    print(f"\nPáginas com texto: {len(documentos)}")

    if documentos:
        primeiro = documentos[0]

        print(f"\nArquivo: {primeiro['arquivo']}")
        print(f"Página: {primeiro['pagina']}")
        print(primeiro["texto"][:1000])
