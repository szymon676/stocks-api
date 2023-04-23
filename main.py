from tradingview_ta import TA_Handler, Interval, Exchange
from fastapi import FastAPI

app = FastAPI()

@app.get("/recommendation/{stock}")
def handle_recommendation(stock: str):
    recom = switch(stock)
    return recom

def tesla_stock() -> str:
    tesla = TA_Handler(
        symbol="TSLA",
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY
    )

    recom = tesla.get_analysis().summary["RECOMMENDATION"]
    return "recommendation for tesla: {}".format(recom)

def appl_stock() -> str:
    aapl = TA_Handler(
        symbol="AAPL",
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY
    )

    recom = aapl.get_analysis().summary["RECOMMENDATION"]
    return "recommendation for apple: {}".format(recom)

def nflx_stock() -> str:
    nflx = TA_Handler(
        symbol="NFLX",
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_DAY
    )

    recom = nflx.get_analysis().summary["RECOMMENDATION"]
    return "recommendation for netflix: {}".format(recom)


def switch(stock: str) -> str:
    match stock:
        case "tesla":
            return tesla_stock()
        case "apple":
            return appl_stock()
        case "netflix":
            return nflx_stock()

# cli
def main():
    while True:
        choice = str(input("choose your stock recomendation: \n Tesla \n Apple \n Netflix \n")).lower()
        print(switch(choice))

if __name__ == "__main__":
    main()