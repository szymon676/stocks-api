from tradingview_ta import TA_Handler, Interval, Exchange
from fastapi import FastAPI

app = FastAPI()

@app.get("/recommendation/{stock}")
def handle_recommendation(stock: str):
    try:
        recom = getStockRecommendation(stock)
    except:
        return "wrong stock name"
    return {"data":{"stockname":stock,"recommendation":recom}}

def getStockRecommendation(stockname: str) -> str:
    stock = TA_Handler(
         symbol=f'{stockname}',
         screener="america",
         exchange="NASDAQ",
         interval=Interval.INTERVAL_1_MINUTE 
     )

    recom = stock.get_analysis().summary["RECOMMENDATION"]
    return recom


def main():
    while True:
        stockname = str(input("write your stock to get recomendation: ")).upper()
        print(getStockRecommendation(stockname))

if __name__ == "__main__":
    main()
