import ConfigParser
import os

def saveToFile(folder_name, file_name, content):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    f = open(os.path.join(folder_name,file_name), "w")
    f.write(content)
    f.close()

def loadConfig(config_file_name):
    config = ConfigParser.RawConfigParser()
    config.read(config_file_name)
    return config
