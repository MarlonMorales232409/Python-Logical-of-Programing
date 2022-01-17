import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=33.969670000000065&lon=-118.249935")

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_="tombstone-container")

print(items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())

period_names = [item.find(class_="period-name").get_text() for item in items]
short_desc = [item.find(class_="short-desc").get_text() for item in items]
temp = [item.find(class_="temp").get_text() for item in items]

weather_stuff = pd.DataFrame({
    "period": period_names,
    "short descriptions": short_desc,
    "temperature": temp,
})

weather_stuff.to_csv("weather.csv", )

print(weather_stuff)
