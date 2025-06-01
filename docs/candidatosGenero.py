import pandas as pd
import plotly.express as px
import streamlit as st

# Função que lê e processa os dados do CSV
def abrir_dados_processados():
    dados = pd.read_csv("dados/CandidatoGenero.csv")
    
    # derretendo a tabela para ter colunas Ano, Gênero, Status, Quantidade
    dados_processados = dados.melt(
        id_vars=["Ano", "Gênero"],
        value_vars=["Aptos", "Inaptos"],
        var_name="Status",
        value_name="Quantidade",
    )
    # coluna combinada Gênero + Status
    dados_processados["Gênero_Status"] = dados_processados["Gênero"] + " " + dados_processados["Status"]
    
    # pivota para formato wide (ano como index, colunas com combinação gênero-status)
    dados_processados = dados_processados.pivot_table(
        index="Ano", columns="Gênero_Status", values="Quantidade", aggfunc="sum"
    )
    
    return dados_processados


# Função que gera o gráfico, recebe dados processados e ano selecionado
def gerar_grafico(dados_processados, ano_selecionado):
    categorias = [
        "Feminino Aptos", "Feminino Inaptos",
        "Masculino Aptos", "Masculino Inaptos"
    ]
    cores = {
        "Feminino Aptos": "#f99",
        "Feminino Inaptos": "#f55",
        "Masculino Aptos": "#8e0000",
        "Masculino Inaptos": "#a52a2a",
    }
    
    if ano_selecionado == "Todos":
        # soma todos os anos 2022, 2023 e 2024
        linha = dados_processados.loc[[2022, 2023, 2024]].sum()
        titulo = "Distribuição por Gênero - Todos os anos"
    else:
        linha = dados_processados.loc[int(ano_selecionado)]
        titulo = f"Distribuição por Gênero - {ano_selecionado}"

    df_pizza = pd.DataFrame({
        "Categoria": categorias,
        "Quantidade": [linha[cat] for cat in categorias],
    })

    fig = px.pie(
        df_pizza,
        names="Categoria",
        values="Quantidade",
        color="Categoria",
        color_discrete_map=cores,
        title=titulo,
    )
    st.plotly_chart(fig)
