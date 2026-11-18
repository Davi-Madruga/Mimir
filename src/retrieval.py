import numpy as np

from src.embeddings import gerar_embedding
from src.vector_store import carregar_indice

def recuperar_trechos(pergunta, quantidade=5):
    if not pergunta.strip():
        raise ValueError("A pergunta não pode estar vazia.")
    if quantidade <= 0:
        raise ValueError("A quantidade de trechos deve ser maior que zero.")

    vetores, trechos = carregar_indice()
    embedding_pergunta = np.asarray(gerar_embedding(pergunta), dtype=np.float32)

    if embedding_pergunta.ndim != 1 or not np.isfinite(embedding_pergunta).all():
        raise ValueError("O embedding da pergunta deve ser um vetor finito.")
    if vetores.shape[1] != embedding_pergunta.shape[0]:
        raise ValueError("O embedding da pergunta não corresponde ao índice carregado.")

    norma_pergunta = np.linalg.norm(embedding_pergunta)
    normas_trechos = np.linalg.norm(vetores, axis=1)
    if norma_pergunta == 0:
        raise ValueError("O embedding da pergunta não pode ter norma zero.")

    denominadores = normas_trechos * norma_pergunta
    similaridades = np.divide(
        vetores @ embedding_pergunta,
        denominadores,
        out=np.zeros_like(normas_trechos),
        where=denominadores != 0,
    )

    indices = np.argsort(similaridades)[::-1][:quantidade]
    return [
        {**trechos[indice], "similaridade": float(similaridades[indice])}
        for indice in indices
    ]
