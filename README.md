# DashboardPro-Streamlit-Dash

## Descrição

Este projeto é um dashboard interativo desenvolvido com **Streamlit**, projetado para visualização e análise de dados de vendas. A aplicação permite que os usuários carreguem dados, visualizem gráficos interativos e explorem os resultados diretamente no navegador.

## Estrutura do Projeto

- `app/`: Contém os principais arquivos da aplicação.
  - `dataset/`: Pasta dedicada aos dados utilizados no dashboard.
    - `Backup/`: Contém cópias de segurança dos datasets.
  - `pages/`: Pasta com os scripts Python que compõem as diferentes páginas do dashboard.
    - `app.py`: Arquivo principal que inicializa a aplicação Streamlit.
    - `dataset.py`: Lida com a manipulação e carregamento dos dados.
    - `graficos.py`: Contém funções para geração dos gráficos.
    - `utils.py`: Funções utilitárias para suporte ao projeto.
    - `vendas.json`: Dataset de vendas utilizado na aplicação.
- `env/`: Pasta com o ambiente virtual do Python (não incluída no repositório).
- `README.md`: Arquivo de documentação do projeto.
- `requirements.txt`: Arquivo com as dependências necessárias para rodar o projeto.

## Instalação

Para rodar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/DashboardPro-Streamlit-Dash.git
   cd DashboardPro-Streamlit-Dash
## Uso
Após executar o comando acima, a aplicação abrirá em seu navegador padrão. Navegue pelas diferentes páginas para explorar os gráficos e dados de vendas. 

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv env
source env/bin/activate  # No Windows, use `env\Scripts\activate`
```

3. Instale as dependências:
 ```bash
   pip install -r requirements.txt
 ```
4. Execute a aplicação:
 ```bash
 streamlit run app/pages/app.py
 ```
## Uso

Após executar o comando acima, a aplicação abrirá em seu navegador padrão. Navegue pelas diferentes páginas para explorar os gráficos e dados de vendas.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Para isso:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça as alterações necessárias.
4. Faça um commit das suas alterações (`git commit -m 'Adicionei nova feature'`).
5. Faça um push para a branch (`git push origin feature/nova-feature`).
6. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
