import os
from os.path import exists
from pprint import pprint as pp

import yfinance as yf


def getStocksForNames(stocklist):
    # lets go through our socialmedia_tickgraphs and the tickers for the actual graph,
    tickers = yf.Tickers(stocklist)
    for x in stocklist:
        var = tickers.tickers.get(x)
        if not isinstance(var, type(None)):
            print(x + " EXISTS\n")


def getStocksForNames2(stocklist, writedir):
    # lets go through our socialmedia_tickgraphs and the tickers for the actual graph,
    tickers = yf.Tickers(stocklist)

    for x in stocklist:
        # print(x)
        var = tickers.tickers.get(x)
        # print(var)
        if not isinstance(var, type(None)):
            hist = var.history(period="1mo")
            # print(hist)
            if not exists(writedir):
                os.mkdir(writedir)
            # print(writedir + "$" + x + "_hist.csv")
            del hist['Dividends']
            del hist['Stock Splits']
            del hist['Volume']
            del hist['Low']
            del hist['High']
            hist['CloseToOpen'] = (((hist['Close'] - hist['Open']) / hist['Open']) * 100).fillna(0)
            del hist['Close']
            del hist['Open']
            hist.to_csv(writedir + "$" + x + "_hist.csv")


def getStocksForNames3(stocklist, writedir):
    tickers = yf.Tickers(stocklist)

    for x in stocklist:
        var = tickers.tickers.get(x)
        if not isinstance(var, type(None)):
            hist = var.history(period="1mo")
            if not exists(writedir):
                os.mkdir(writedir)
            hist.to_csv(writedir + "$" + x + "_hist.csv")


def doesStockExist(name) -> bool:
    ticker = yf.Ticker(name)
    if not isinstance(ticker, type(None)):
        return True
    return False
