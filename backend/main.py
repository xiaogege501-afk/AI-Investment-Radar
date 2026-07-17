from fastapi import FastAPI
from datetime import datetime


app = FastAPI(
    title="AI Investment Radar",
    description="Crypto + Forex AI Market Intelligence System",
    version="0.1"
)


@app.get("/")
def root():

    return {
        "system": "AI Investment Radar",
        "status": "online",
        "time": datetime.utcnow()
    }


@app.get("/market")

def market():

    return {

        "crypto": [

            {
                "symbol": "BTC",
                "price": 98000,
                "score": 82,
                "trend": "bullish",
                "reason": [
                    "Market momentum positive",
                    "Volume increasing",
                    "Risk acceptable"
                ]
            },

            {
                "symbol": "ETH",
                "price": 3500,
                "score": 76,
                "trend": "neutral"
            }

        ],


        "forex":[

            {
                "symbol":"EUR/USD",
                "price":1.09,
                "score":75,
                "trend":"neutral"
            }

        ]

    }
