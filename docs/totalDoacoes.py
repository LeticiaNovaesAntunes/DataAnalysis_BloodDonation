import pandas as pd

def calcular_total_doacoes(arquivo_csv, ano):
    try:
        df = pd.read_csv(arquivo_csv)

        if not {'Ano', 'Doador', 'Tipo de Exame'}.issubset(df.columns):
            raise ValueError("CSV deve conter as colunas 'Ano', 'Doador' e 'Tipo de Exame'.")

        df = df[df['Tipo de Exame'].str.startswith("ABO / Rh(D)", na=False)]

        if ano != "Todos":
            df = df[df['Ano'] == int(ano)]
        else:
            df = df[df['Ano'].isin([2022, 2023, 2024])]  

        df = df[df['Doador'].notna()]
        df['Doador'] = df['Doador'].astype(int)

        return int(df['Doador'].sum())

    except Exception as e:
        return f"Erro: {e}"
