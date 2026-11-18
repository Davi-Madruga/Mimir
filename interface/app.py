import streamlit as st

from src.facade import MimirFacade


st.set_page_config(page_title="Mimir")
st.title("Mimir")

with st.form("consulta"):
    pergunta = st.text_input("Qual é a sua dúvida sobre RPG?")
    enviar = st.form_submit_button("Consultar")

if enviar:
    if not pergunta.strip():
        st.warning("Digite uma pergunta para consultar os livros.")
    else:
        try:
            with st.spinner("Consultando os livros..."):
                resposta = MimirFacade().consultar(pergunta.strip())
        except FileNotFoundError:
            st.error("Índice não encontrado. Execute python indexar_base.py na raiz do projeto.")
        except ConnectionError:
            st.error("Não foi possível conectar ao Ollama. Confira se ele está em execução.")
        except ValueError as erro:
            st.error(str(erro))
        else:
            st.markdown(resposta)
