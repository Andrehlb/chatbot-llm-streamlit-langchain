import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

st.title("Chatbot com LLM usando Streamlit e LangChain 🚀")

pergunta = st.text_area("Digite sua pergunta aqui:")

if st.button("Enviar"):
    if not pergunta.strip():
        st.warning("Por favor, digite uma pergunta antes de enviar.")
    elif not os.getenv("OPENAI_API_KEY"):
        st.warning(
            "A OPENAI_API_KEY não está configurada. "
            "A aplicação está pronta para usar ChatOpenAI, "
            "mas nenhuma chamada real à API foi feita."
        )
    else:
        llm = ChatOpenAI(model="gpt-5.4 mini")
        resposta = llm.invoke(pergunta)
        
        st.write("Resposta do Chatbot:")
        st.write(resposta.content)