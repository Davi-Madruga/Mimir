from .llm import gerar_resposta
from .retrieval import recuperar_trechos


def responder_pergunta(pergunta, quantidade=5):
    trechos = recuperar_trechos(pergunta, quantidade)

    if not trechos:
        raise ValueError("O retrieval não encontrou trechos para responder.")

    return gerar_resposta(pergunta, trechos)
