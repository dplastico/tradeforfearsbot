import requests

def high(coin):
    coins = [coin]
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=USD&limit=10".format(",".join(coins))).json()["RAW"]
    return crypto_data[coin.upper()]["USD"]["PRICE"]