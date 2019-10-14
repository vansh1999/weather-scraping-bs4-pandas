import pandas as pd

import requests

from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=36.3741&lon=-119.2702#.XaTObB9fg5k')

soup = BeautifulSoup(page.content , 'html.parser')

week = soup.find(id = "seven-day-forecast-body")

items = week.find_all(class_ = 'tombstone-container')


# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_ = 'temp temp-high').get_text())

period_name =   [item.find(class_ = 'period-name').get_text() for item in items]
# print(period_name)

short_desc = [item.find(class_ = 'short-desc').get_text() for item in items]
# print(short_desc)

temp_high = [item.find(class_ = 'temp').get_text() for item in items]
# print(temp_high)



weather_stuff = pd.DataFrame({

    'period' : period_name,
    'short_des' : short_desc,
    'temp' : temp_high,

})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
