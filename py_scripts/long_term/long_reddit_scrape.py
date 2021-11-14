import os
import re
from os.path import exists

import praw

# interpret data over month
from long_term.LongGraph import LongGraph
from long_term.LongPoint import LongPoint
from stock_scrape import doesStockExist


def interpretData(subreddit, tickMap):
    for post in subreddit.top("month", limit=1):

        potential_tickers = set()
        finds = re.findall(r'[$][A-Za-z]+', post.title)

        # For each ticker in a post we need a point, for every comment under this post each of those tickers gets .5 a count
        # if that comment contains the ticker, they get 1 + the .5 as well
        # if a ticker is in the title it gets 5 points
        #
        #

        if finds.count != 0:
            potential_tickers.update(finds)

        for tickName in potential_tickers:
            tickName = tickName.upper()
            if doesStockExist(tickName):
                if tickName not in tickMap:
                    tickMap[tickName] = LongGraph(tickName)
                tickMap[tickName].addLongPoint(LongPoint(post.created_utc))
                tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(5)
        title_tickers = set()
        title_tickers.update(potential_tickers)

        #print("Ticks for post: " + str(title_tickers))
        # Do comments
        post.comment_sort = "top"
        top_level_comments = list(post.comments)
        for comment in top_level_comments:
            potential_tickers = set()
            if hasattr(comment, "body"):
                finds = re.findall(r'[$][A-Za-z]+', comment.body)
                potential_tickers.update(finds)
                # add them to the relevant place
                if hasattr(comment, "created_utc"):
                    for tickName in potential_tickers:
                        tickName = tickName.upper()
                        if doesStockExist(tickName):
                            if tickName not in tickMap:
                                tickMap[tickName] = LongGraph(tickName)
                                tickMap[tickName].addLongPoint(LongPoint(comment.created_utc))
                            tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(1)
                #print("Ticks in comment: "+ str(potential_tickers))
            # count # of comments
            for title_ticker in title_tickers:
                title_ticker = title_ticker.upper()
                if doesStockExist(title_ticker):
                    tickMap[title_ticker].graphList[len(tickMap[title_ticker].graphList) - 1].addCount(.5)
                #print("Incrementing: "+title_ticker)

def writeGraphs(graph):
    name = graph.name
    dirname = "socialmedia_tickgraphs_long/"
    if not exists(dirname):
        os.mkdir(dirname)
    filename = "socialmedia_tickgraphs_long/" + name + "_graph.csv"
    f = open(filename, "w")
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
    subreddits = ["Superstonk", "wallstreetbets", "stocks", "investing", "pennystocks", "robinhood", "InvestmentClub"]

    tickMap = dict()
    for x in subreddits:
        subreddit = reddit.subreddit(x)
        interpretData(subreddit, tickMap)

    for graph in tickMap:
        writeGraphs(tickMap[graph])


main()
