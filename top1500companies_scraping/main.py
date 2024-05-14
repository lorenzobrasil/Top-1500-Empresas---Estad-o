from bs4 import BeautifulSoup
import pandas as pd

with open(r"./top1500companies_scraping/data/Empresas Mais 2023.html", 'r', encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content, 'html.parser')

bs4_companies = soup.select('.TabelaHeader>div')

pandas_objects = []


# Retirando o primeiro registro (nome das colunas)
bs4_companies = bs4_companies[1:]

# Transformando as empresas em dicionários
for company_index, company_html_tag in enumerate(bs4_companies):
    new_company = {}

    # Colunas não escondidas
    html_class_cols = ['numero',
                       'nome',
                       'col-setor',
                       'col-regiao',
                       'col-cie']
    for dim_index in range(len(html_class_cols)):
      try:
        company_html_tag.select("div.{}".format(html_class_cols[dim_index]))[0].text
        new_company[html_class_cols[dim_index]] = company_html_tag.select(".{}".format(html_class_cols[dim_index]))[0].text
      except:
        continue
      

    # Colunas escondidas
    hidden_tags = company_html_tag.select('div.boxrolar div.item')
    for hidden_tag in hidden_tags:
      new_company[hidden_tag.select('div.titulo')[0].text] = hidden_tag.select('div.info')[0].text
    
    pandas_objects += [new_company]
    
    
# Export para um Pandas DataFrame
df = pd.DataFrame(data=pandas_objects)
df.to_excel('./top1500companies_scraping/data/ranking_1500_empresas.xlsx')