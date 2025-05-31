import streamlit as st
import candidatosGenero
import candidatosIdade

# Candidatos por gênero
st.title("Análise de Aptos e Inaptos por Gênero e Ano")
candidatosGenero.gerar_grafico(candidatosGenero.abrir_dados_processados())

# Candidatos por idade
st.title("Análise de candidatos por idade")
candidatosIdade.gerar_grafico(candidatosIdade.abrir_dados_processados())
