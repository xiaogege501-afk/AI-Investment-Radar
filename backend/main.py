from fastapi import FastAPI
from datetime import datetime


app = FastAPI(
    title="AI Investment Radar",
    version="0.1"
)


@app.get("/")
def home():

    return {
        "system": "AI Investment Radar",
        "status": "online",
        "time": datetime.utcnow()
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
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
                "trend": "neutral",
                "reason": [
                    "Stable ecosystem",
                    "Moderate demand"
                ]
            }

        ],


        "forex": [

            {
                "symbol": "EUR/USD",
                "price": 1.09,
                "score": 75,
                "trend": "neutral",
                "reason": [
                    "USD pressure",
                    "Macro uncertainty"
                ]
            }

        ]

    }
