# grafico.py
import streamlit as st
import pandas as pd
import plotly.express as px

def exibir_grafico_doadores_por_ano(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)

        # Verifica colunas obrigatórias
        if not {'Ano', 'Doador', 'Tipo de Exame'}.issubset(df.columns):
            st.error("CSV deve conter as colunas 'Ano', 'Doador' e 'Tipo de Exame'.")
            return

        # Filtra exames do tipo ABO / Rh(D)
        df = df[df['Tipo de Exame'].str.startswith("ABO / Rh(D)", na=False)]
        df = df[df['Doador'].notna()]
        df['Doador'] = df['Doador'].astype(int)


        df_ano = df.groupby('Ano')['Doador'].sum().reset_index().sort_values('Ano')

        # Gráfico
        fig = px.line(df_ano, x='Ano', y='Doador',
                      title='Total de Doadores por Ano',
                      color_discrete_sequence=['#8e0000'] ,
                      markers=True)
        fig.update_layout(xaxis_title="Ano", yaxis_title="Número de Doadores")

        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Erro ao gerar gráfico: {e}")
