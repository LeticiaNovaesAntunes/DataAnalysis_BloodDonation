import streamlit as st
from totalDoacoes import calcular_total_doacoes
import candidatosGenero
import candidatosIdade 
from doacaoPorAno import exibir_grafico_doadores_por_ano
import os

st.set_page_config(page_title="...", layout="wide")
st.title("🩸 Análise de Doações de Sangue no Estado de SP")

col1, col2 = st.columns(2)

with col1:

   

    # Filtro Ano
    ano_selecionado = st.sidebar.selectbox(
        "Ano",
        ("Todos", "2022", "2023", "2024")
    )

    # Caminho do arquivo CSV (corrigido com os.path para compatibilidade)
    caminho_csv = os.path.join("dados", "ImunoHematologia.csv")

    # Chama a função do outro módulo
    total_doacoes = calcular_total_doacoes(caminho_csv, ano_selecionado)
    

    # Exibe cartão com total de doações
    if isinstance(total_doacoes, int):
        st.markdown(
            f"""
            <div style="background-color:#8e0000; padding:30px; items-align: center; border-radius:10px; width:300px">
                <h4 style="color:white;">Total de Doações</h4>
                <h1 style="color:white;">{total_doacoes:,}</h1>
                <p style="color:white;">Ano: <strong>{ano_selecionado}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error(total_doacoes)

with col2:
        #Gráfico analis doação nos anos

    if caminho_csv is not None:
        exibir_grafico_doadores_por_ano(caminho_csv)



# Gráfico de candidatos por gênero
try:
    # abrir_dados_processados() só carrega e processa os dados, não recebe argumentos
    dados_processados = candidatosGenero.abrir_dados_processados()
    
    # gerar_grafico recebe os dados processados e o ano selecionado
    candidatosGenero.gerar_grafico(dados_processados, ano_selecionado)
except Exception as e:
    st.error(f"Erro ao gerar gráfico de gênero: {e}")


#Gráfico Idade dos doadores
try:
    dados_processados_idade = candidatosIdade.abrir_dados_processados()
    candidatosIdade.gerar_grafico(dados_processados_idade, ano_selecionado)
except Exception as e:
    st.error(f"Erro ao gerar gráfico de idade: {e}")
 


 