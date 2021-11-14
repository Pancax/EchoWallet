import os
from os.path import exists
from shutil import copy

from stock_scrape import getStocksForNames2

fileName= "../data_generate/long_term/socialmedia_tickgraphs_long"

files = os.listdir(fileName)

fileCounts = []
#we want the 20 best graphs, so lets just count the x axis and return best one
for file in files:
    st = open(fileName+"/"+file,"r")
    lines = st.readlines()
    fileCounts.append((file,len(lines)))

i=0
fileCounts.sort(key=lambda tup: tup[1],reverse=True)
bestFiles = []
for count in fileCounts:
    if i<50:
        bestFiles.append(count[0])
        i+=1


#make pruned graphs
for file in bestFiles:
    dirname="pruned_graphs/"
    if not exists(dirname):
        os.mkdir(dirname)
    destfile = "pruned_graphs/" + file
    f = open(destfile, "w")
    rf = open(fileName+"/"+file,"r")

    f.write("Date,Count\n")
    f.close()
    f = open(destfile, "a")
    f.writelines(rf.readlines())
    f.close()
    rf.close()

stockNames=[]
for file in bestFiles:
    file = file.replace("$","")
    file = file.replace("_graph.csv","")
    stockNames.append(file)

getStocksForNames2(stockNames,"pruned_graph_hists/")

