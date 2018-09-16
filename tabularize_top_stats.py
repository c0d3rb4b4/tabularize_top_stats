import fileinput
import pandas
from matplotlib import pyplot

def fr(t):
    return t

file_prefix = 'proc_table'

def metDictToTablePandas(metDict, fileName):
    df = pandas.DataFrame(metDict)
    df = df.cumsum()
    plot = df.plot()
    fig = plot.get_figure()
    fig.savefig(fileName)
    pyplot.close('all')
    return df.to_string()

currentTimestamp = ''
cpuMetDict = {}
memMetDict = {}
for line in fileinput.input():
    lineArray = line.strip().split()

    if (currentTimestamp != '') and (lineArray[0] != currentTimestamp):
        cpuFile = file_prefix + '_cpu_' + lineArray[0].replace(':', '') + '.csv'
        memFile = file_prefix + '_mem_' + lineArray[0].replace(':', '') + '.csv'

        cpuImageFile = file_prefix + '_cpu_' + lineArray[0].replace(':', '') + '.png'
        memImageFile = file_prefix + '_mem_' + lineArray[0].replace(':', '') + '.png'
        cpuTable = str(metDictToTablePandas(cpuMetDict, cpuImageFile)).replace("NaN", ' -1')
        print '****CPU Table****'
        print cpuTable

        memTable = str(metDictToTablePandas(memMetDict, memImageFile)).replace("NaN", ' -1')
        print '****Mem Table****'
        print memTable

        f = open(cpuFile, "w")
        f.write(cpuTable)
        f.close()

        f = open(memFile, "w")
        f.write(memTable)
        f.close()

    if lineArray[1] not in cpuMetDict:
        cpuMetDict[lineArray[1]] = {}
        memMetDict[lineArray[1]] = {}
    currentTimestamp = lineArray[0]
    cpuMetDict[lineArray[1]][lineArray[0]] = float(lineArray[2])
    memMetDict[lineArray[1]][lineArray[0]] = float(lineArray[3])
