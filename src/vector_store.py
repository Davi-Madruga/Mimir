import json
import numpy as np

from pathlib import Path
from tempfile import NamedTemporaryFile


ARQUIVO_INDICE = Path(__file__).resolve().parents[1] / "data/vector_store/indice.npz"


def indexar_chunks(chunks, caminho=ARQUIVO_INDICE):
    if not chunks:
        raise ValueError("A lista de chunks está vazia.")

    vetores = np.asarray([chunk["embedding"] for chunk in chunks], dtype=np.float32)
    if vetores.ndim != 2 or vetores.shape[1] == 0 or not np.isfinite(vetores).all():
        raise ValueError("Cada embedding deve ser um vetor de números finitos.")

    trechos = []
    for chunk in chunks:
        trecho = chunk.copy()
        del trecho["embedding"]
        trechos.append(trecho)

    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=caminho.parent, delete=False) as temporario:
        arquivo_temporario = Path(temporario.name)
    try:
        with arquivo_temporario.open("wb") as arquivo:
            np.savez(arquivo, vetores=vetores, trechos=json.dumps(trechos, ensure_ascii=False))
        arquivo_temporario.replace(caminho)
    finally:
        arquivo_temporario.unlink(missing_ok=True)

    return caminho


def carregar_indice(caminho=ARQUIVO_INDICE):
    with np.load(caminho, allow_pickle=False) as indice:
        return indice["vetores"], json.loads(indice["trechos"].item())
