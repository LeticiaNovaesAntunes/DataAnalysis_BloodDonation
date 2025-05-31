import streamlit as st
import pandas as pd
import plotly.express as px

# variaveis com colunas das tabelas
col_ano = "Ano"
col_genero = "Gênero"
col_aptos = "Aptos"
col_inaptos = "Inaptos"
col_status = "Status"
col_quantidade = "Quantidade"
col_genero_status = "Gênero_Status"
col_fem_aptos = "Feminino Aptos"
col_fem_inaptos = "Feminino Inaptos"
col_masc_aptos = "Masculino Aptos"
col_masc_inaptos = "Masculino Inaptos"

# Variaveis de cores do grafico
cor_fem_aptos = "#f99"
cor_fem_inaptos = "#f55"
cor_masc_aptos = "#99f"
cor_masc_inaptos = "#55f"


def abrir_dados_processados():
    dados = pd.read_csv("./docs/dados/CandidatoGenero.csv")

    # Gera nova tabela utilizando a CandidatoGenero.csv, com colunas: Ano, Gênero, Status, Quantidade
    dados_processados = dados.melt(
        id_vars=[col_ano, col_genero],
        value_vars=[col_aptos, col_inaptos],
        var_name=col_status,
        value_name=col_quantidade,
    )
    # Cria uma nova coluna combinado Gênero e Status para usar como colunas
    dados_processados[col_genero_status] = (
        dados_processados[col_genero] + " " + dados_processados[col_status]
    )

    # Agora pivotamos para formato wide: linhas = Ano, colunas = 'Genero_Status', valores = Quantidade
    dados_processados = dados_processados.pivot_table(
        index=col_ano, columns=col_genero_status, values=col_quantidade, aggfunc="sum"
    )
    return dados_processados


def gerar_grafico(dados_processados):
    # Filtro por ano
    anos = dados_processados.index.unique()
    ano_selecionado = st.selectbox("Selecione o ano", anos, key="CandidatosGenero")

    # Filtrar linha do ano escolhido
    linha = dados_processados[dados_processados.index == ano_selecionado].iloc[0]

    categorias = [col_fem_aptos, col_fem_inaptos, col_masc_aptos, col_masc_inaptos]
    cores_personalizadas = {
        col_fem_aptos: cor_fem_aptos,
        col_fem_inaptos: cor_fem_inaptos,
        col_masc_aptos: cor_masc_aptos,
        col_masc_inaptos: cor_masc_inaptos,
    }
    # Organizar dados para o gráfico de pizza
    dados_pizza = pd.DataFrame(
        {
            "Categoria": categorias,
            "Quantidade": [
                linha[col_fem_aptos],
                linha[col_fem_inaptos],
                linha[col_masc_aptos],
                linha[col_masc_inaptos],
            ],
        }
    )

    # Criar gráfico de pizza com Plotly
    fig = px.pie(
        dados_pizza,
        names="Categoria",
        values="Quantidade",
        category_orders={"Categoria": categorias},
        color="Categoria",
        color_discrete_map=cores_personalizadas,
        title=f"Distribuição por Gênero e Situação - {ano_selecionado}",
    )

    st.plotly_chart(fig)
