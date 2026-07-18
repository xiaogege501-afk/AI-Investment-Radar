from scoring import analyze_market
from crypto import get_market
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="AI Investment Radar"
)


@app.get("/", response_class=HTMLResponse)
def home():

    return """

    <html>

    <head>

    <title>
    AI Investment Radar
    </title>


    <style>

    body{

    background:#0b1220;
    color:white;
    font-family:Arial;
    padding:40px;

    }


    .card{

    background:#172033;
    padding:20px;
    margin:15px;
    border-radius:15px;

    }


    </style>

    </head>


    <body>


    <h1>
    AI Investment Radar
    </h1>


    <div class="card">

    <h2>
    Crypto Market
    </h2>


    BTC

    <br>

    Price:
    $98,000


    <br>

    AI Score:
    82


    <br>

    Trend:
    Bullish


    </div>




    <div class="card">

    <h2>
    Forex Market
    </h2>


    EUR/USD


    <br>

    Price:
    1.09


    <br>

    AI Score:
    75


    </div>




    <div class="card">


    <h2>
    AI Report
    </h2>


    Market condition:

    Positive momentum.


    </div>


    </body>

    </html>

    """


@app.get("/api/status")
@app.get("/api/crypto")
def crypto():

    market=get_market()


    result=[]


    for coin in market:


        change=(

            coin["price"]

            -

            coin["open24h"]

        ) / coin["open24h"] *100



        analysis=analyze_market(change)



        result.append({

            "symbol":
            coin["symbol"],


            "price":
            coin["price"],


            "change":
            round(change,2),


            "analysis":
            analysis

        })


    return {

        "market":result

    }
def status():

    return {

        "system":"AI Investment Radar",

        "status":"running"

    }
