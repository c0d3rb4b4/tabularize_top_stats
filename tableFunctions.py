import pandas
from matplotlib import pyplot
import os

def metDictToDataFrame(metDict):
    return pandas.DataFrame(metDict)

def plotDataFrame(df, plotFileName):
    plot = df.plot(marker='o')
    handles, labels = plot.get_legend_handles_labels()
    lgd = plot.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-.05), ncol=5, borderaxespad=0.)
    plot.grid(True)
    fig = plot.get_figure()
    fig.savefig(plotFileName, bbox_extra_artists=(lgd,), bbox_inches='tight')
    pyplot.close('all')

def metDictToTable(metDict, folder_name, plotFileName):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    df = metDictToDataFrame(metDict)
    plotDataFrame(df, os.path.join(folder_name, plotFileName))
    return df.to_string().replace("NaN", '   ')
