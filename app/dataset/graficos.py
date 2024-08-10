import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por estado',
    height = 500,  # Ajuste a altura do gráfico
    width = 800  # Ajuste a largura do gráfico
)

grafico_rec_mensal = px.bar(
    df_rec_mensal,
    x = "Mes",
    y = "Preço",
    color = 'Ano',
    title = 'Receita Mensal'
)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

# grafico_rec_mensal = px.line(
#     df_rec_mensal,
#     x = "Mes",
#     y = "Preço",
#     markers = True,
#     range_y = (0, df_rec_mensal.max()),
#     color = 'Ano',
#     line_dash = 'Ano',
#     title = 'Receita Mensal'
# )

grafico_rec_estado = px.bar(
    df_rec_estado.head(10),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top 10 Receita por Estado'
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(10),
    orientation='h',  # Definindo a orientação horizontal
    text_auto = True,
    title = 'Top 10 Categorias por Receita'
)

# grafico_rec_vendedores = px.bar(
#     # df_vendedores[['sum']].sort_values('sum', ascending=True).head(5),
#     df_vendedores.sort_values('sum', ascending=True).head(5),
#     x='sum',
#     # y = df_vendedores[['sum']].sort_values('sum', ascending=True).head(5).index,
#     y = df_vendedores.sort_values('sum', ascending=True).head(5).index,
#     text_auto=True,
#     title='Top 10 Vendedores por Receita'
# )

# Ordena os vendedores pela receita em ordem decrescente
grafico_rec_vendedores = px.bar(
    df_vendedores,
    x='sum',
    y=df_vendedores.index,
    text_auto=True,
    title='Top 10 Vendedores por Receita'
)




