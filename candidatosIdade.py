import streamlit as st
import pandas as pd

# variaveis com colunas das tabelas
col_ano = "Ano"
col_faixa_etaria = "Faixa Etária"
col_aptos = "Aptos"
col_inaptos = "Inaptos"

# Variaveis de cores do grafico
cor_aptos = "#f99"
cor_inaptos = "#f55"


def abrir_dados_processados():
    dados = pd.read_csv("./docs/dados/CandidatoIdade.csv")

    dados_processados = dados
    dados_processados[col_faixa_etaria] = dados_processados[col_faixa_etaria].replace(
        {"< 18 anos": "18 anos ou menos", "≥ 29 anos": "29 anos ou maior"}
    )

    return dados_processados


def gerar_grafico(dados_processados):
    anos = dados_processados[col_ano].unique()
    ano_selecionado = st.selectbox("Selecione o ano", anos, key="CandidatosIdade")

    stack = st.toggle("Exibir gráfico empilhado")

    dados_filtrado = dados_processados[dados_processados[col_ano] == ano_selecionado]

    st.bar_chart(
        data=dados_filtrado,
        x=col_faixa_etaria,
        y=[col_aptos, col_inaptos],
        stack=stack,
        color=[cor_aptos, cor_inaptos],
    )
