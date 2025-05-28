import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Natasha é uma diva :)", layout="centered")

st.title("📊 Natasha é uma diva")

# Dados para gráficos de barra e coluna
df = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valor': [10, 23, 15, 7]
})

# Dados para gráfico de linha
df_line = pd.DataFrame({
    'Dia': pd.date_range(start='2025-05-01', periods=7),
    'Valor': [10, 12, 9, 14, 18, 13, 17]
})

# Abas para os gráficos
aba1, aba2, aba3 = st.tabs(["📉 Barras Horizontais", "📊 Colunas Verticais", "📈 Linha Interativa"])

with aba1:
    st.subheader("Gráfico de Barras Horizontais")
    fig_bar = px.bar(df,
                     x='Valor',
                     y='Categoria',
                     orientation='h',
                     title='Barras Horizontais',
                     color_discrete_sequence=['#ff69b4'])
    fig_bar.update_layout(plot_bgcolor='white', title_font_color='#ff69b4')
    st.plotly_chart(fig_bar)

with aba2:
    st.subheader("Gráfico de Colunas Verticais")
    fig_col = px.bar(df,
                     x='Categoria',
                     y='Valor',
                     title='Colunas Verticais',
                     color_discrete_sequence=['#ff1493'])  # rosa escuro
    fig_col.update_layout(plot_bgcolor='white', title_font_color='#ff1493')
    st.plotly_chart(fig_col)

with aba3:
    st.subheader("Gráfico de Linha Interativo")
    fig_line = px.line(df_line,
                       x='Dia',
                       y='Valor',
                       markers=True,
                       title='Linha Temporal',
                       color_discrete_sequence=['#ff69b4'])
    fig_line.update_layout(plot_bgcolor='white', title_font_color='#ff69b4')
    st.plotly_chart(fig_line)