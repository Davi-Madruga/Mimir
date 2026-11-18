import re
import unicodedata
import numpy as np

from .embeddings import gerar_embedding
from .vector_store import carregar_indice

PALAVRAS_IGNORADAS = {
    "a", "as", "ao", "aos", "com", "da", "das", "de", "do", "dos",
    "e", "é", "em", "o", "os", "para", "por", "que", "um", "uma",
}


def _normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.casefold())
    texto = "".join(caractere for caractere in texto if not unicodedata.combining(caractere))
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()


def _extrair_frase_alvo(pergunta):
    frase = _normalizar(pergunta)

    prefixos = (
        "o que e ", "o que significa ", "qual e ", "quem e ",
        "explique ", "defina ", "fale sobre ",
    )
    for prefixo in prefixos:
        if frase.startswith(prefixo):
            frase = frase[len(prefixo):]
            break

    return frase


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

    frase_alvo = _extrair_frase_alvo(pergunta)
    termos_alvo = {
        termo for termo in frase_alvo.split()
        if termo not in PALAVRAS_IGNORADAS and len(termo) > 1
    }

    relevancias = []
    for similaridade, trecho in zip(similaridades, trechos):
        texto_normalizado = _normalizar(trecho.get("texto", ""))
        termos_encontrados = termos_alvo.intersection(texto_normalizado.split())
        cobertura = len(termos_encontrados) / len(termos_alvo) if termos_alvo else 0
        frase_encontrada = bool(frase_alvo) and frase_alvo in texto_normalizado

        # A correspondência lexical complementa o embedding, especialmente
        # para nomes próprios e títulos de magias presentes nos livros.
        relevancia = float(similaridade) + (0.15 * cobertura)
        if frase_encontrada:
            relevancia += 0.20
        relevancias.append(relevancia)

    indices = np.argsort(relevancias)[::-1][:quantidade]
    return [
        {
            **trechos[indice],
            "similaridade": float(similaridades[indice]),
            "relevancia": float(relevancias[indice]),
        }
        for indice in indices
    ]
