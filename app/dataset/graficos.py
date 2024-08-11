import plotly.express as px

def grafico_map_estado(df_rec_estado):
    return px.scatter_geo(
        df_rec_estado,
        lat='lat',
        lon='lon',
        scope='south america',
        size='Preço',
        template='seaborn',
        hover_name='Local da compra',
        hover_data={'lat': False, 'lon': False},
        title='Receita por estado',
        height=500,
        width=800
    )

def grafico_rec_mensal(df_rec_mensal):
    return px.bar(
        df_rec_mensal,
        x="Mes",
        y="Preço",
        color='Ano',
        title='Receita Mensal'
    )

def grafico_rec_estado(df_rec_estado):
    return px.bar(
        df_rec_estado.head(10),
        x='Local da compra',
        y='Preço',
        text_auto=True,
        title='Top 10 Receita por Estado'
    )

def grafico_rec_categoria(df_rec_categoria):
    return px.bar(
        df_rec_categoria.head(10),
        orientation='h',  # Definindo a orientação horizontal
        text_auto=True,
        title='Top 10 Categorias por Receita'
    )

def grafico_rec_vendedores(df_vendedores):
    return px.bar(
        df_vendedores.sort_values('sum', ascending=False).head(10).iloc[::-1],
        x='sum',
        y=df_vendedores.sort_values('sum', ascending=False).head(10).iloc[::-1].index,
        text_auto=True,
        title='Top 10 Vendedores por Receita'
    )

def grafico_vendas_vendedores(df_vendedores):
    return px.bar(
        df_vendedores[["count"]].sort_values('count').tail(10),
        x='count',
        y=df_vendedores[["count"]].sort_values('count').tail(10).index,
        text_auto=True,
        title='Top 10 Vendedores por Vendas'
    )