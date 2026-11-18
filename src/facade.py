from .chunking import chunking
from .embeddings import adicionar_embeddings
from .loader import buscar_pdfs, ler_documentos
from .rag import responder_pergunta
from .vector_store import indexar_chunks


class MimirFacade:
    def indexar_base(self, pasta):
        arquivos = buscar_pdfs(pasta)
        documentos = ler_documentos(arquivos)
        chunks = chunking(documentos)
        chunks = adicionar_embeddings(chunks)

        return indexar_chunks(chunks)

    def consultar(self, pergunta):
        return responder_pergunta(pergunta)