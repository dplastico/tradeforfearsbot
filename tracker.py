import requests


def hello():
    return "Hello World!!!"

def prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }
    return data

def price(coin):
    coins = [coin]
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]
    return crypto_data[coin.upper()]["USD"]["PRICE"]

if __name__ == "__main__":
        print(get_prices())

