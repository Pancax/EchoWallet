import os
from os.path import exists

import yfinance as yf
from pandas import DataFrame

ticker = yf.Ticker("LCID")


hist = ticker.history(period="1mo")
dirname = "stockhist/"
if not exists(dirname):
    os.mkdir(dirname)
hist.to_csv("stockhist/$LCID_hist.csv")