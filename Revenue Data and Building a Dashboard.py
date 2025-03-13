import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour créer des graphiques
def make_graph(stock_data, revenue_data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], label="Stock Price", color="blue")
    plt.plot(revenue_data['Date'], revenue_data['Revenue'], label="Revenue", color="red")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price/Revenue")
    plt.legend()
    plt.grid(True)
    plt.show()  

# Question 1: Extraire les données boursières de Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print("Tesla Stock Data:")
print(tesla_data.head())

# Question 2: Extraire les données de revenus de Tesla
url_tesla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response_tesla = requests.get(url_tesla)
soup_tesla = BeautifulSoup(response_tesla.text, "html.parser")

# Trouver la table des revenus
table_tesla = soup_tesla.find("table")  # Utilisez la bonne balise ou classe si nécessaire
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

if table_tesla:
    for row in table_tesla.find_all("tr"):  # Parcourir chaque ligne
        cols = row.find_all("td")  # Parcourir chaque cellule
        if len(cols) >= 2:  # Vérifier qu'il y a au moins deux colonnes
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print("\nTesla Revenue Data:")
print(tesla_revenue.head())

# Question 3: Extraire les données boursières de GameStop
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print("\nGameStop Stock Data:")
print(gme_data.head())

# Question 4: Extraire les données de revenus de GameStop
url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
response_gme = requests.get(url_gme)
soup_gme = BeautifulSoup(response_gme.text, "html.parser")

# Trouver la table des revenus
table_gme = soup_gme.find("table")  # Utilisez la bonne balise ou classe si nécessaire
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

if table_gme:
    for row in table_gme.find_all("tr"):  # Parcourir chaque ligne
        cols = row.find_all("td")  # Parcourir chaque cellule
        if len(cols) >= 2:  # Vérifier qu'il y a au moins deux colonnes
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().replace("$", "").replace(",", "")
            gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print("\nGameStop Revenue Data:")
print(gme_revenue.head())

# Question 5: Créer un graphique pour Tesla
make_graph(tesla_data, tesla_revenue, 'Tesla Stock and Revenue Dashboard')

# Question 6: Créer un graphique pour GameStop
make_graph(gme_data, gme_revenue, 'GameStop Stock and Revenue Dashboard')

# Question 7: Partager le code sur GitHub
print("\nLe code a été exécuté avec succès. Fin de l'exercice'!")