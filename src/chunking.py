def chunking(documentos, tamanho_chunk=1100, sobreposicao=100):
    if tamanho_chunk <= 0:
        raise ValueError("tamanho_chunk deve ser maior que zero.")
    if not 0 <= sobreposicao < tamanho_chunk:
        raise ValueError("sobreposicao deve ser >= 0 e menor que tamanho_chunk.")

    chunks = []

    for documento in documentos:
        texto = documento["texto"]
        inicio = 0
        numero = 1

        while inicio < len(texto):
            fim = inicio + tamanho_chunk
            trecho = texto[inicio:fim]

            if trecho.strip():
                chunk = documento.copy()
                chunk["texto"] = trecho
                chunk["chunk"] = numero
                chunks.append(chunk)
                numero += 1

            if fim >= len(texto):
                break

            inicio = fim - sobreposicao

    return chunks
