from dataset import df
import pandas as pd
import streamlit as st
import time

def format_number(value, prefix = " "):
    for unit in ['', 'mil']:
        if value < 1000:
            return f"{prefix} {value:.2f} {unit}"
        value /= 1000
    return f"{prefix} {value:.2f} milhões"

def gerar_dataframes_derivados(df):
    # Recriar DataFrame Receita por Estado
    df_rec_estado_agg = df.groupby('Local da compra')[["Preço"]].sum()
    df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
    df_rec_estado = df_rec_estado.merge(df_rec_estado_agg, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

    # Recriar DataFrame Receita Mensal
    df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
    df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
    df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()

    # Recriar DataFrame Receita por Categoria
    df_rec_categoria = df.groupby("Categoria do Produto")[["Preço"]].sum().sort_values("Preço", ascending=True)

    # Recriar DataFrame Vendedores
    df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

    return df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# Função para converter arquivo csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon="✅"
        )
    time.sleep(3)
    success.empty()
