# Web Scraping

Este script em Python realiza web scraping no site [keychronbrasil.com.br](https://keychronbrasil.com.br) para coletar informações sobre teclados, incluindo título, preço original e preço com desconto. Os dados são armazenados em uma planilha Excel.

## Bibliotecas Utilizadas

- **requests:** Usada para fazer solicitações HTTP e obter o conteúdo da página web.
- **BeautifulSoup:** Utilizada para realizar a análise HTML da página web e extrair informações específicas.
- **openpyxl:** Utilizada para criar e manipular planilhas Excel.

## Funcionamento do Script

1. O script cria uma nova planilha Excel chamada "teclados.xlsx".
2. Faz solicitações HTTP para cada página do site que lista teclados, coletando títulos, preços originais e preços com desconto.
3. Os dados são inseridos na planilha Excel.
4. A planilha é salva na pasta "data" como "teclados.xlsx".

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `BeautifulSoup`, `openpyxl`

## Instruções de Uso

1. Instale as bibliotecas necessárias executando o comando: `pip install requests beautifulsoup4 openpyxl`.
2. Execute o script em um ambiente Python.

*Lembre-se de que web scraping pode estar sujeito aos termos de serviço de um site. Certifique-se de cumprir todas as regras e políticas do site que você está acessando. Este script foi desenvolvido para fins educacionais e pode precisar ser ajustado conforme necessário.*
