import streamlit as st
import pandas as pd
import plotly.express as px

def abrir_dados_processados():
    df = pd.read_csv("dados/inaptidao.csv", encoding="utf-8")
    df.columns = df.columns.str.strip()

    return df

def gerar_grafico(df, ano_selecionado):
    # Verifica se colunas essenciais existem
    colunas_esperadas = {"Causa", "Ano", "Masculino", "Feminino"}
    colunas_reais = set(df.columns)

    if not colunas_esperadas.issubset(colunas_reais):
        st.error(f"Colunas ausentes no DataFrame: {colunas_esperadas - colunas_reais}")
        st.text(f"Colunas reais no CSV: {list(df.columns)}")
        return

    if ano_selecionado != "Todos":
        df = df[df["Ano"] == int(ano_selecionado)]

    if df.empty:
        st.warning("Nenhum dado encontrado para o ano selecionado.")
        return

    df_melted = df.melt(
        id_vars=["Causa", "Ano"],
        value_vars=["Masculino", "Feminino"],
        var_name="Sexo",
        value_name="Quantidade"
    )

    # Gráfico
    fig = px.bar(
        df_melted,
        x="Causa",
        y="Quantidade",
        color="Sexo",
        barmode="stack",
        title=f"Inaptidão por Causa",
        color_discrete_sequence=["#8e0000", "#f99"]  ,
        labels={"Causa": "Motivo", "Quantidade": "Total", "Sexo": "Sexo"},
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Dados Filtrados")
    st.dataframe(df)

def main():
    st.title("Gráfico de Inaptidão na Triagem")
    df = abrir_dados_processados()

    anos = sorted(df["Ano"].dropna().unique().tolist())
    anos_str = [str(ano) for ano in anos]
    anos_str.insert(0, "Todos")

    ano_selecionado = st.selectbox("Filtrar por Ano:", anos_str)
    gerar_grafico(df, ano_selecionado)

if __name__ == "__main__":
    main()
