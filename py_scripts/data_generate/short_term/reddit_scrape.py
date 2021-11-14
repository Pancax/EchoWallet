import datetime
import os
import time
from os.path import exists
import text2emotion as te
import praw
import re
from data_generate.short_term.Ticker import Ticker
from stock_scrape import getStocksForNames, doesStockExist


def main():
    # reddit client instance
    reddit = praw.Reddit(client_id='icbpfsrP79uW1oxRKokBPg', client_secret='pId-cGSHUhKuRji_vYfF_cyuheSHPg',
                         user_agent='EchoScraper')
    reddit.read_only = True

    # lets say this, run
    # read all of our comments/threads/post
    # aggregate into a count, give that count a timestap, then we can construct a graph based on it
    # wait an hour repeat

    subreddits = ["Superstonk", "wallstreetbets", "stocks", "investing", "pennystocks", "robinhood", "InvestmentClub"]
    while True:
        tickMap = dict()
        for x in subreddits:
            subreddit = reddit.subreddit(x)
            interpret_data(subreddit, tickMap)
        for ticker in tickMap:
            write_ticker_to_graph(tickMap[ticker])
        keyList = []
        keyList.extend(tickMap.keys())
        getStocksForNames(keyList)
        time.sleep(900)


def interpret_data(subreddit, tickMap):
    # list of string, to Ticker.py

    # tickMap
    # $TSLA, 10, 305pm
    # $LCID, 7, 305pm
    # TSLA_GRAPH.csv
    # 10, 305pm
    # LCID_GRAPH.csv
    # 7, 305pm
    for post in subreddit.hot(limit=20):

        # do title
        potential_tickers = set()
        title_tickers = set()
        finds = re.findall(r'[$][A-Za-z]+', post.title)
        if finds.count != 0:
            potential_tickers.update(finds)

        for tickName in potential_tickers:
            tickName = tickName.upper()
            if doesStockExist(tickName):
                if tickName not in tickMap:
                    tickMap[tickName] = Ticker(tickName)
                analysis = te.get_emotion(post.title)
                tickMap[tickName].add_instance(post.created_utc, analysis)

        # print(potential_tickers)
        title_tickers.update(potential_tickers)

        # Do comments
        post.comment_sort = "top"
        top_level_comments = list(post.comments)
        for comment in top_level_comments:
            potential_tickers = set()
            # get our matches inside comments
            if hasattr(comment, "body"):
                finds = re.findall(r'[$][A-Za-z]+', comment.body)
                potential_tickers.update(finds)
                # add them to the relevant place
                if hasattr(comment, "created_utc"):
                    for tickName in potential_tickers:
                        tickName = tickName.upper()
                        if doesStockExist(tickName):
                            if tickName not in tickMap:
                                tickMap[tickName] = Ticker(tickName)
                            analysis = te.get_emotion(comment.body)
                            tickMap[tickName].add_instance(comment.created_utc, analysis)

            # count # of comments
            for title_ticker in title_tickers:
                if doesStockExist(title_ticker):
                    title_ticker = title_ticker.upper()
                    tickMap[title_ticker].add_comment()


def write_ticker_to_graph(ticker):
    name = ticker.name
    dirname = "socialmedia_tickgraphs_short/"
    if not exists(dirname):
        os.mkdir(dirname)
    filename = "socialmedia_tickgraphs_short/" + name + "_graph.csv"
    f = open(filename, "a")
    line = str((ticker.finalX + datetime.datetime.utcnow()) / 2) + "," + str(
        len(ticker.list) + ticker.comCount / .5) + "," + str(ticker.finalZ) + "\n"

    f.write(line)
    f.close()


main()
