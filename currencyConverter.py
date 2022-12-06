import json
from bs4 import BeautifulSoup
import requests

config_file = open('config.json')
data = json.load(config_file)

from_currency = data["from_currency"]
to_currency = data["to_currency"]
amount = data["amount"]


def get_currency():
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"  # UrL
    content = requests.get(url).text  # Take all the html page into text
    soup = BeautifulSoup(content, 'html.parser')  # create the soup object
    currency = soup.find('p', {
        'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'}).get_text()  # find the element and get the text
    return currency  # return it


if __name__ == "__main__":
    conversion = get_currency()
    print(f"{amount} {from_currency} is equal to {conversion}")
