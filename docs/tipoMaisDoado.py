import pandas as pd
import plotly.express as px
import streamlit as st

def abrir_dados_processados():
    df = pd.read_csv("dados/ImunoHematologia.csv")
    df["Doador"] = pd.to_numeric(df["Doador"], errors="coerce")
    df["Receptor"] = pd.to_numeric(df["Receptor"], errors="coerce")
    df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
    df["Tipo de Exame"] = df["Tipo de Exame"].astype(str)
    return df

def gerar_grafico(df, ano_selecionado):
    tipos = df["Tipo de Exame"].dropna().unique().tolist()
    tipos_selecionados = st.multiselect("Filtrar por Tipo de Exame:", tipos, default=tipos)

    df_filtrado = df[df["Tipo de Exame"].isin(tipos_selecionados)]

    if ano_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Ano"] == int(ano_selecionado)]

    if df_filtrado.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
        return

    df_melted = df_filtrado.melt(
        id_vars=["Tipo de Exame", "Ano"],
        value_vars=["Doador", "Receptor"],
        var_name="Grupo",
        value_name="Quantidade"
    )

    fig = px.bar(
        df_melted,
        y="Tipo de Exame",
        x="Quantidade",
        color="Grupo",
        facet_col="Ano" if ano_selecionado == "Todos" else None,
        orientation="h",
        barmode="group",
        title="Comparação entre Doadores e Receptores por Tipo de Exame",
        color_discrete_sequence=["#8e0000", "#f55"]  ,
        height=600
    )
    
    

    st.plotly_chart(fig)
    st.dataframe(df_filtrado)