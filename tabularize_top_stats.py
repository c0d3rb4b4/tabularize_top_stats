import fileinput
import utils
import tableFunctions

def generateFileNames(file_prefix, currentTimestamp):
    cpuFileName = file_prefix + '_cpu_' + currentTimestamp.replace(':', '')
    memFileName = file_prefix + '_mem_' + currentTimestamp.replace(':', '')
    return cpuFileName, memFileName

currentTimestamp = ''
cpuMetDict = {}
memMetDict = {}
config = utils.loadConfig('config.ini')
for line in fileinput.input():
    lineArray = line.strip().split()

    if config.getboolean('cfg', 'save_continous_stream') and (currentTimestamp != '') and (lineArray[0] != currentTimestamp):
        cpuFile, memFile = generateFileNames(config.get('cfg', 'file_prefix'), lineArray[0])
        cpuTable = tableFunctions.metDictToTable(cpuMetDict, config.get('cfg','folder_name'), cpuFile + '.svg')
        memTable = tableFunctions.metDictToTable(memMetDict, config.get('cfg','folder_name'), memFile + '.svg')
        utils.saveToFile(config.get('cfg','folder_name'), cpuFile + '.csv', cpuTable)
        utils.saveToFile(config.get('cfg','folder_name'), memFile + '.csv', memTable)
        print 'Saved for timestamp ' + lineArray[0]

    if lineArray[1] not in cpuMetDict:
        cpuMetDict[lineArray[1]] = {}
        memMetDict[lineArray[1]] = {}
    currentTimestamp = lineArray[0]
    cpuMetDict[lineArray[1]][lineArray[0]] = float(lineArray[2])
    memMetDict[lineArray[1]][lineArray[0]] = float(lineArray[3])

if config['save_static'] and cpuMetDict and memMetDict:
    cpuFile, memFile = generateFileNames(config['file_prefix'], currentTimestamp)
    cpuTable = tableFunctions.metDictToTable(cpuMetDict, config.get('cfg','folder_name'), cpuFile + '.svg')
    memTable = tableFunctions.metDictToTable(memMetDict, config.get('cfg','folder_name'), memFile + '.svg')
    utils.saveToFile(config[folder_name], cpuFile + '.csv', cpuTable)
    utils.saveToFile(config[folder_name], memFile + '.csv', memTable)
