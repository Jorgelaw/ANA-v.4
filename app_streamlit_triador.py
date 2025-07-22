import streamlit as st
import openai
from script_vetorizacao import vetorizar_modelos
from script_busca_similaridade import buscar_modelos_similares

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Assistente Triador")
st.write("Envie um processo em PDF. A ANA vai identificar o(s) modelo(s) mais semelhantes e gerar a minuta.")

uploaded_file = st.file_uploader("Faça upload do processo em PDF", type="pdf")

if uploaded_file:
    with open("processo.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("Arquivo recebido. Analisando...")

    vetor_modelo, nomes_modelos = vetorizar_modelos("modelos.csv")
    resultado = buscar_modelos_similares("processo.pdf", vetor_modelo, nomes_modelos)

    st.write("Modelo(s) mais semelhante(s):")
    st.write(resultado["modelos"])
    st.write("Minuta sugerida:")
    st.write(resultado["minuta"])