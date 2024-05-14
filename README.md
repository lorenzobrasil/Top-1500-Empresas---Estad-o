# Objetivo

Extrair os indicadores contábeis e financeiros das empresas disponibilizados pelo Ranking Mais Empresas do Estadão (https://publicacoes.estadao.com.br/empresasmais/ranking-1500/)

# Método
O projeto a princípio deveria extrair todo o HTML via requisição HTTP (módulo requests). No entanto, como é uma página dinâmica, isso só seria possível de maneira automatizada utilizando Selenium. Para facilitar, extrai o HTML (depois de carregar todas as informações) pelo próprio browser e salvei dentro do diretório de dados (./top1500companies_scraping/data).

Sugiro reprodução dos passos acima (com os devidos ajustes das tags e estrutura HTML no tratamento das páginas), caso deseja atingir o mesmo em situação similar.

# Instalação e Uso

## Pré-requisitos

Para o funcionamento do projeto é necessário ter instalado na máquina:
1. [Python](https://www.python.org/)
2. [Poetry](https://python-poetry.org/)


## Projeto

Com o Poetry instalado, basta clonar este repositório e executar na raiz:

```bash
poetry build
poetry install
```

Com o projeto Poetry montado, para iniciá-lo basta executar o comando

```bash
start_scraping
```