import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import numpy as np
import time

url = 'https://www.divan.ru/category/divany-i-kresla'  # Или конкретная страница

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # <---- ОБНОВИТЕ ЭТИ СЕЛЕКТОРЫ НА ОСНОВЕ HTML-КОДА
    divans = soup.find_all('div', class_='lsooF')
    prices = []
    for divan in divans:
        try:
            price_element = divan.find('span', class_='ui-LD-ZU KIkOH')
            if price_element:
                price_text = price_element.text.replace(' ', '').replace('₽', '').replace('руб.', '').strip() # Удаляем "руб."
                try:
                    price = float(price_text)
                    prices.append(price)
                except ValueError:
                    print(f"Ошибка преобразования цены: {price_text}")
            else:
                print("Элемент цены не найден в карточке.")
        except AttributeError as e:
            print(f"Ошибка при поиске цены: {e}")

    print("Найденные цены:", prices)

    if prices:
        with open('divan_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Цена'])
            for price in prices:
                writer.writerow([price])
        print("Цены сохранены в divan_prices.csv")

        average_price = np.mean(prices)
        print(f"Средняя цена: {average_price:.2f} ₽")

        plt.figure(figsize=(10, 6))
        plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
        plt.title('Распределение цен на диваны')
        plt.xlabel('Цена (₽)')
        plt.ylabel('Количество')
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    else:
        print("Не удалось извлечь цены.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")