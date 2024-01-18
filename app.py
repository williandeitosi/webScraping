import requests
from bs4 import BeautifulSoup
import os
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet.title = "Teclados"
sheet["A1"] = "Teclados"
sheet["B1"] = "Preço"
sheet["C1"] = "Preço com desconto"

i = 1
row = 2
while True:
    url = f"https://keychronbrasil.com.br/collections/teclados?page={i}"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        titles = soup.find_all("div", class_="grid-product__title")
        original_prices = soup.find_all("span", class_="grid-product__price--original")
        discount_prices = soup.find_all("span", class_="sale-price")
        
        if titles:
            for title, price, discount in zip(titles, original_prices, discount_prices):
                title_text = title.get_text(strip=True)
                
                price_text = price.get_text(strip=True)
                price_format = float(price_text.split()[-1].replace('.', '').replace(',', '.'))
                
                discount_text = discount.get_text(strip=True)
                discount_format = float(discount_text.split()[-1].replace('.', '').replace(',', '.'))
                
                sheet[f"A{row}"] = title_text
                sheet[f"B{row}"] = price_format
                sheet[f"C{row}"] = discount_format
                
                row += 1
            i += 1
        else:
            print("Não há mais páginas disponíveis.")
            break

    else:
        print(f"A solicitação falhou com status {response.status_code}")
        break

for col in ['B', 'C']:
    for row in range(2, sheet.max_row + 1):
        cell = sheet[f"{col}{row}"]
        cell.number_format = 'R$ #,##0.00'

pasta = "data"
if not os.path.exists(pasta):
    os.mkdir(pasta)
    print(f"A pasta {pasta} foi criada com sucesso!")
else:
    print(f"A pasta {pasta} já existe")

workbook.save(f"{pasta}/teclados.xlsx")
