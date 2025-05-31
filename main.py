import streamlit as st
import candidatosGenero

# Candidatos por gênero
st.title("Análise de Aptos e Inaptos por Gênero e Ano")
candidatosGenero.gerar_grafico(candidatosGenero.abrir_dados_processados())
