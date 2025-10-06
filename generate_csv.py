import requests
import csv

url = "https://restcountries.com/v3.1/all?fields=name,population,area,region"
response = requests.get(url)
data = response.json()

with open('paises.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
    
    for country in data:
        nombre = country['name']['common']
        poblacion = country.get('population', 0)
        superficie = country.get('area', 0)
        continente = country.get('region', '')
        writer.writerow([nombre, poblacion, superficie, continente])