import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores,grafico_vendas_vendedores

# st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Vem pra lua",
    page_icon="🌛",
    layout="wide",
    initial_sidebar_state="auto"
)
st.title("Dashboard de Vendas :shopping_trolley:")

st.sidebar.title('Filtro de Vendedores')
filtro_vendedor = st.sidebar.multiselect(
    "Vendedores",
    df["Vendedor"].unique()
)

if filtro_vendedor:
    df = df[df["Vendedor"].isin(filtro_vendedor)]

st.sidebar.title('Filtro de Pagamento')
filtro_pagamento = st.sidebar.multiselect(
    "Tipo de pagamento",
    df["Tipo de pagamento"].unique()
)

if filtro_pagamento:
    df = df[df["Tipo de pagamento"].isin(filtro_pagamento)]



st.sidebar.title('Filtro de Local')
filtro_local = st.sidebar.multiselect(
    "Local da compra",
    df["Local da compra"].unique()
)

if filtro_local:
    df = df[df["Local da compra"].isin(filtro_local)]



aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        receita_total = df["Preço"].sum()
        st.metric("Receita Total", format_number(receita_total, "R$"))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        quantidade_vendas = df.shape[0]
        st.metric("Quantidade de Vendas", format_number(quantidade_vendas))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores, use_container_width=True)