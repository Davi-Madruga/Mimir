# Mimir
Mimir é um sistema de busca e consulta para RPGs, utilizando RAG para recuperar informações de regras, mundos, personagens, criaturas e outros conteúdos a partir de livros e documentos em uma base de dados.

## Estrutura do projeto

A pasta raiz deste repositório corresponde a `mimir/`:

```text
mimir/
├── src/
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── llm.py
│   └── rag.py
├── data/
│   ├── raw/
│   └── vector_store/
├── interface/
│   └── app.py
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Responsabilidades

- `src/loader.py`: carregar livros e documentos.
- `src/chunking.py`: dividir documentos em trechos.
- `src/embeddings.py`: gerar vetores para trechos e consultas.
- `src/vector_store.py`: armazenar e consultar vetores.
- `src/retrieval.py`: recuperar contexto relevante.
- `src/llm.py`: integrar o modelo de linguagem.
- `src/rag.py`: coordenar o fluxo RAG.
- `interface/app.py`: disponibilizar a interface de uso.
- `data/raw/`: guardar os documentos de entrada.
- `data/vector_store/`: guardar o índice vetorial persistido.
- `tests/`: reunir os testes do projeto.

## Estado atual

Estrutura inicial: os módulos contêm apenas descrições de suas responsabilidades.
O fluxo RAG e a interface ainda precisam ser implementados; as dependências serão
definidas nessa etapa.

O arquivo `.env` guarda configurações locais e é ignorado pelo Git. Em um novo
clone, crie esse arquivo na raiz conforme as configurações necessárias.
Os arquivos `.gitkeep` preservam as pastas vazias no controle de versão.
