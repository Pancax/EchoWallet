from os.path import exists

from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
# our two graphs are in data_clean/pruned_graph_hists
# and pruned_graphs
import os

import pandas

from stock_scrape import getStocksForNames3

databoys = []

# databoys is a list of tuples(name, graph, hist)

histdirpath = "../data_clean/pruned_graph_hists/"
graphdirpath = "../data_clean/pruned_graphs/"

# this wont work unless pruned graph and hists are deleted every time they are generated but whatever

outputfilepath = "predictions/"
if not exists(outputfilepath):
    os.mkdir(outputfilepath)

histfiles = os.listdir(histdirpath)
graphfiles = os.listdir(graphdirpath)

for index, item in enumerate(histfiles):
    name = item.replace("$", "")
    name = name.replace("_hist.csv", "")
    histo = pandas.read_csv(histdirpath + item)
    grapho = pandas.read_csv(graphdirpath + graphfiles[index])
    databoys.append((name, grapho, histo))

newdataboys = []
for data in databoys:

    avgR=0.0
    avgOther=0.0
    runonce=True
    for _ in range(50):
        if len(data[1])>len(data[2]):
            sampleData = data[1].sample(len(data[2]), replace=False)
            regress = stats.pearsonr(sampleData['Count'], data[2]['CloseToOpen'])
            avgR+=regress[0];
            avgOther+=regress[1];

            if(runonce):
                X = sampleData['Count']
                Y = data[2]['CloseToOpen']

                X = sm.add_constant(X)

                model = sm.OLS(list(Y), X, missing='drop')
                model_result=model.fit()
                ax = plt.subplot()
                fig = sm.graphics.plot_fit(model_result,1,vlines=False,ax=ax)
                ax.set_ylabel("Percent Change in Price")
                ax.set_xlabel("Social Media Score");
                ax.set_title("Predictions Based On Social Media Score")
                fig.savefig(outputfilepath+data[0]+".png")
                plt.close()
                del fig
                runonce=False
        elif len(data[1])<len(data[2]):
            sampleData = data[2].sample(len(data[1]), replace=False)
            regress = stats.pearsonr(data[1]['Count'], sampleData['CloseToOpen'])

            avgR+=regress[0];
            avgOther+=regress[1];

            if runonce:
                X = data[1]['Count']
                Y = sampleData['CloseToOpen']

                X = sm.add_constant(X)

                model = sm.OLS(list(Y), X, missing='drop')
                model_result=model.fit()
                ax = plt.subplot()
                fig = sm.graphics.plot_fit(model_result,1,vlines=False,ax=ax)
                ax.set_ylabel("Percent Change in Price")
                ax.set_xlabel("Social Media Score");
                ax.set_title("Predictions Based On Social Media Score")
                fig.savefig(outputfilepath+data[0]+".png")
                plt.close()
                del fig
                runonce=False
        else:
            regress = stats.pearsonr(data[1]['Count'], data[2]['CloseToOpen'])
            avgR+=regress[0];
            avgOther+=regress[1];

            if runonce:

                X = data[1]['Count']
                Y = data[2]['CloseToOpen']

                X = sm.add_constant(X)

                model = sm.OLS(list(Y), X, missing='drop')
                model_result=model.fit()
                ax = plt.subplot()
                fig = sm.graphics.plot_fit(model_result,1,vlines=False,ax=ax)
                ax.set_ylabel("Percent Change in Price")
                ax.set_xlabel("Social Media Score");
                ax.set_title("Predictions Based On Social Media Score")
                fig.savefig(outputfilepath+data[0]+".png")
                plt.close()
                del fig
                runonce=False
    avgR/=50;
    avgOther/=50;




    #print(Y)
    #print(X)

    #print(model_result.rsquared)

    #print(model_result.summary())


    newdataboys.append((data[0],data[1],data[2],avgR,avgOther))

    # print("Corr: "+sampleData.corrwith(data[1]))
    # print(data)

newdataboys.sort(key=lambda tup: tup[3], reverse=True)


outfile = open(outputfilepath+"top_predictions.txt","w")
graphswewant = []
i=0;
for data in newdataboys:
    if i<10:
        line = data[0]+ ", Rsquared: "+ str(data[3])+"\n"
        outfile.write(line)
        graphswewant.append(data[0])
    i+=1;

outfile.close()

getStocksForNames3(graphswewant,"finalgraphs/")