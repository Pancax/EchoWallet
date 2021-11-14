import os
import re
from os.path import exists

import praw

# interpret data over month
from long_term.LongGraph import LongGraph
from long_term.LongPoint import LongPoint
from stock_scrape import doesStockExist



def interpretData(subreddit, tickMap, symbolsF):

    for post in subreddit.top("month", limit=5):

        potential_tickers = set()

        symbolSet= set()
        for symbol in symbolsF:
            symbol = symbol.replace("\n","")
            symbol2 = "$"+symbol
            symbolSet.add(symbol)
            symbolSet.add(symbol2)

        wordsTitle = set()
        wordsTitle.update(re.findall(r'\$*\w+', post.title));
        wordsText = set()
        wordsText.update(re.findall(r'\$*\w+', post.selftext));

        for word in wordsTitle:
            if word in symbolSet and ("$" in word or not len(word)<=3):
                if("$" in word):
                    potential_tickers.add(word)
                else:
                    potential_tickers.add("$"+word)
        for word in wordsText:
            if word in symbolSet and ("$" in word or not len(word)<=3):
                if("$" in word):
                    potential_tickers.add(word)
                else:
                    potential_tickers.add("$"+word)

            #thing = re.search("\\s+" + re.escape(symbol) + "[\\s+\\.]",post.title)
            #thing2 = re.search("\\s+"+re.escape(symbol2)+"[\\s+\\.]",post.title)
            #thing3 = re.search("\\s+"+re.escape(symbol)+"[\\s+\\.]",post.selftext)
            #thing4 = re.search("\\s+"+re.escape(symbol2)+"[\\s+\\.]",post.selftext)
            #if thing and len(symbol)>3 or thing2 or thing3 and len(symbol)>3 or thing4:
            #    potential_tickers.add(symbol2)



        #finds = re.findall(r'[$][A-Za-z]+', post.title)
        #finds2 = re.findall(r'[$][A-Za-z]+', post.selftext)
        # For each ticker in a post we need a point, for every comment under this post each of those tickers gets .5 a count
        # if that comment contains the ticker, they get 1 + the .5 as well
        # if a ticker is in the title it gets 5 points
        #
        #
        #if finds.count != 0:
        #    potential_tickers.update(finds)
        #    print(finds)
        #if finds2.count != 0:
        #    potential_tickers.update(finds2)
        #    print(finds2)

        print(post.title)
        print(post.selftext)
        print(potential_tickers)

        for tickName in potential_tickers:
            tickName = tickName.upper()
            if doesStockExist(tickName):
                if tickName not in tickMap:
                    tickMap[tickName] = LongGraph(tickName)
                tickMap[tickName].addLongPoint(LongPoint(post.created_utc))
                tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(100)
        title_tickers = set()
        title_tickers.update(potential_tickers)

        #print("Ticks for post: " + str(title_tickers))
        # Do comments
        post.comment_sort = "top"
        top_level_comments = list(post.comments)
        # count # of comments
        for title_ticker in title_tickers:
            title_ticker = title_ticker.upper()
            if doesStockExist(title_ticker):
                tickMap[title_ticker].graphList[len(tickMap[title_ticker].graphList) - 1].addCount(len(top_level_comments))

        for comment in top_level_comments:
            potential_tickers = set()
            if hasattr(comment, "body"):
                wordsBody = set()
                wordsBody.update(re.findall(r'\$*\w+', comment.body));
                for word in wordsBody:
                    if word in symbolSet and ("$" in word or not len(word)<=3):
                        if("$" in word):
                            potential_tickers.add(word)
                        else:
                            potential_tickers.add("$"+word)

                # add them to the relevant place
                if hasattr(comment, "created_utc"):
                    for tickName in potential_tickers:
                        tickName = tickName.upper()
                        if doesStockExist(tickName):
                            if tickName not in tickMap:
                                tickMap[tickName] = LongGraph(tickName)
                            tickMap[tickName].addLongPoint(LongPoint(comment.created_utc))
                            print("Tick in comment, adding 10: " +tickName)
                            tickMap[tickName].graphList[len(tickMap[tickName].graphList) - 1].addCount(10)


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
    subreddits = ["Superstonk", "wallstreetbets", "stocks", "investing", "pennystocks", "robinhood", "InvestmentClub", "bitcoin", "CryptoMoonshots","cryptomarkets","options","wallstreetbetselite","wallstreetbetsnew","spacs","daytrading"]
    symbolsF = open("../../resources/stocksymbols/stocksymbols.txt","r").readlines()
    print(symbolsF)
    tickMap = dict()
    for x in subreddits:
        subreddit = reddit.subreddit(x)
        interpretData(subreddit, tickMap,symbolsF)

    for graph in tickMap:
        writeGraphs(tickMap[graph])


main()
