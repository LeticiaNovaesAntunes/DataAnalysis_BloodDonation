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
    dados = pd.read_csv("dados/CandidatoIdade.csv")
    
  
    dados_processados = dados
    dados_processados[col_faixa_etaria] = dados_processados[col_faixa_etaria].replace(
            {"< 18 anos": "18 anos ou menos", "≥ 29 anos": "29 anos ou maior"}
        )

    return dados_processados


def gerar_grafico(dados_processados, ano_selecionado):
    if ano_selecionado == "Todos":
        dados_filtrado = (
        dados_processados[dados_processados['Ano'].isin([2022, 2023, 2024])]
        .groupby(col_faixa_etaria)[[col_aptos, col_inaptos]]
        .sum()
        .reset_index()
    )
    else:
        dados_filtrado = dados_processados[dados_processados['Ano'] == int(ano_selecionado)]

    st.markdown(f"<h3 style='font-size: 18px; font-style: bold;'>Idade dos Doadores - {ano_selecionado}</h3>", unsafe_allow_html=True)
    stack = st.toggle("Exibir gráfico empilhado")

    st.bar_chart(
        data=dados_filtrado,
        x=col_faixa_etaria,
        y=[col_aptos, col_inaptos],
        stack=stack,
        color=[cor_aptos, cor_inaptos],
    )
