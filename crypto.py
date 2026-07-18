import requests


def get_crypto_price(symbol):

    url = "https://www.okx.com/api/v5/market/ticker"


    params = {

        "instId": f"{symbol}-USDT"

    }


    response = requests.get(
        url,
        params=params,
        timeout=10
    )


    data = response.json()


    if data["code"] == "0":

        ticker = data["data"][0]


        return {

            "symbol":symbol,

            "price":float(ticker["last"]),

            "change":

            ticker["open24h"]

        }


    return None



def get_market():

    coins = [

        "BTC",

        "ETH",

        "SOL"

    ]


    result=[]


    for coin in coins:

        price=get_crypto_price(coin)


        if price:

            result.append(price)


    return result
