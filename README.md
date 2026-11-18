#INTEGRANTES
Davi Farias
Luis Gabriel 
José Ricardo

# Como rodar o Mimir no Windows

## 1. Confira o Python e o Git

Abra o PowerShell e execute os comandos abaixo. O projeto usa Python 3.12.

```powershell
py -3.12 --version
git --version
```

Se algum comando falhar, instale o programa correspondente, abra um novo PowerShell e confira a versão novamente. [Baixar Python para Windows](https://www.python.org/downloads/windows/) · [Baixar Git para Windows](https://git-scm.com/downloads/win)

## 2. Instale o Ollama e baixe o modelo

Instale e abra o [Ollama para Windows](https://ollama.com/download/windows). Em um novo PowerShell, baixe o modelo usado pelo Mimir e aguarde a conclusão.

```powershell
ollama pull qwen3:4b
```

Mantenha o Ollama em execução enquanto estiver consultando os livros.

## 3. Clone o repositório e instale as dependências

```powershell
git clone https://github.com/Davi-Madruga/rag-rpg.git
cd rag-rpg
py -3.12 -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 4. Adicione os PDFs e gere o índice

Copie seus livros em PDF para `data/raw/`. Em `indexar_base.py`, substitua a linha que define `PASTA_PDFS` pela seguinte e salve o arquivo.

```python
PASTA_PDFS = Path(__file__).parent / "data" / "raw"
```

Na raiz do repositório, execute o comando abaixo. Na primeira execução, o projeto baixa o modelo de embeddings `all-MiniLM-L6-v2` e processa os PDFs, incluindo os das subpastas.

```powershell
.\venv\Scripts\python.exe indexar_base.py
```

Aguarde a mensagem `Índice salvo em` antes de abrir a interface. Repita a indexação quando adicionar, alterar ou remover PDFs.

## 5. Inicie a interface

Na raiz do repositório, execute:

```powershell
.\venv\Scripts\python.exe -m streamlit run interface/app.py
```

Abra o endereço indicado como `Local URL` no terminal, digite uma pergunta e clique em **Consultar**. Nas próximas sessões, basta abrir o Ollama e repetir o comando desta etapa se os PDFs continuarem os mesmos.
