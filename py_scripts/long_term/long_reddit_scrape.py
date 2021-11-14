import os
import re
from os.path import exists

import praw

# interpret data over month
from long_term.LongGraph import LongGraph
from long_term.LongPoint import LongPoint
from stock_scrape import doesStockExist

tickMap = dict()


def interpretData(subreddit, symbolsF):
    for post in subreddit.top("month", limit=5):

        potential_tickers = set()

        symbolSet = set()
        for symbol in symbolsF:
            symbol = symbol.replace("\n", "")
            symbol2 = "$" + symbol
            symbolSet.add(symbol)
            symbolSet.add(symbol2)

        wordsTitle = set()
        wordsTitle.update(re.findall(r'\$*\w+', post.title));
        wordsText = set()
        wordsText.update(re.findall(r'\$*\w+', post.selftext));

        for word in wordsTitle:
            if word in symbolSet and ("$" in word or not len(word) <= 3):
                if ("$" in word):
                    potential_tickers.add(word)
                else:
                    potential_tickers.add("$" + word)
        for word in wordsText:
            if word in symbolSet and ("$" in word or not len(word) <= 3):
                if ("$" in word):
                    potential_tickers.add(word)
                else:
                    potential_tickers.add("$" + word)

        #print(post.title)
        #print(post.selftext)
        #print(potential_tickers)

        for tickName in potential_tickers:
            tickName = tickName.upper()
            if tickName not in tickMap:
                tickMap[tickName] = LongGraph(tickName)
            tickMap[tickName].addLongPoint(LongPoint(post.created_utc))
            tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(100)
            #print("count after title: "+str(tickName) + ""+str(tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].count))
        title_tickers = set()
        title_tickers.update(potential_tickers)

        # print("Ticks for post: " + str(title_tickers))
        # Do comments
        post.comment_sort = "top"
        top_level_comments = list(post.comments)
        # count # of comments
        for title_ticker in title_tickers:
            title_ticker = title_ticker.upper()
            tickMap[title_ticker].graphList[len(tickMap[title_ticker].graphList) - 1].addCount(len(top_level_comments))
           #print("count after # of coments: "+str(title_ticker) + ""+str(tickMap[title_ticker].graphList[len(tickMap[title_ticker].graphList) - 1].count))

        for comment in top_level_comments:
            potential_tickers = set()
            if hasattr(comment, "body"):
                wordsBody = set()
                wordsBody.update(re.findall(r'\$*\w+', comment.body));
                for word in wordsBody:
                    if word in symbolSet and ("$" in word or not len(word) == 1):
                        if ("$" in word):
                            potential_tickers.add(word)
                        else:
                            potential_tickers.add("$" + word)

                # add them to the relevant place
                if hasattr(comment, "created_utc"):
                    for tickName in potential_tickers:
                        tickName = tickName.upper()
                        if tickName not in tickMap:
                            tickMap[tickName] = LongGraph(tickName)
                        tickMap[tickName].addLongPoint(LongPoint(comment.created_utc))
                       # print("Tick in comment, adding 10: " + tickName)
                        tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(10)
                       # print("count after comment: "+str(tickName) + ""+str(tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].count))
                # print("Incrementing: "+title_ticker)


def writeGraphs(graph):
    name = graph.name
    dirname = "socialmedia_tickgraphs_long/"
    if not exists(dirname):
        os.mkdir(dirname)
    filename = "socialmedia_tickgraphs_long/" + name + "_graph.csv"
    f = open(filename, "w")
    graph.makeGraphGood()
    for point in graph.graphList:
        line = str(point.time) + "," + str(point.count) + "\n"
        f.write(line)

    f.close()


def main():
    # reddit client instance
    reddit = praw.Reddit(client_id='icbpfsrP79uW1oxRKokBPg', client_secret='pId-cGSHUhKuRji_vYfF_cyuheSHPg',
                         user_agent='EchoScraper')
    reddit.read_only = True

    # this take in the reddit results in a longer timeframe
    subreddits = ["Superstonk", "wallstreetbets", "stocks", "investing", "pennystocks", "robinhood", "InvestmentClub",
                  "bitcoin", "CryptoMoonshots", "cryptomarkets", "options", "wallstreetbetselite", "wallstreetbetsnew",
                  "spacs", "daytrading"]
    symbolsF = open("../../resources/stocksymbols/stocksymbols.txt", "r").readlines()
    print(symbolsF)

    for x in subreddits:
        subreddit = reddit.subreddit(x)
        interpretData(subreddit, symbolsF)

    for graph in tickMap:
        writeGraphs(tickMap[graph])


main()
