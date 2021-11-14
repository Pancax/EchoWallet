import os
from os.path import exists

import yfinance as yf
from pandas import DataFrame


names = ["LCID","TSLA","GOOG","AAPL","X","TOUR"]
tickers = yf.Tickers(names)

for name in names:
    hist = tickers.tickers.get(name).history(period="1mo")
    dirname = "stockhist/"
    if not exists(dirname):
        os.mkdir(dirname)
    hist.to_csv("stockhist/$"+name+"_hist.csv")