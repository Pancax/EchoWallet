from pprint import pprint as pp

import yfinance as yf


def getStocksForNames(stocklist):
    # lets go through our socialmedia_tickgraphs and the tickers for the actual graph,
    tickers = yf.Tickers(stocklist)
    for x in stocklist:
        var = tickers.tickers.get(x)
        if not isinstance(var, type(None)):
            print(x + " EXISTS\n")


def doesStockExist(name) -> bool:
    ticker = yf.Ticker(name)
    if not isinstance(ticker, type(None)):
        return True
    return False
