'''
Created on 16.07.2018

@author: wang
'''
import zipfile
import os
STR_BASE_PATH, STR_MODULE_NAME = os.path.split(__file__)


def fileCrawler(strPath="", ltExtensions=('.txt')):
    rtsFiles = []
    if strPath == "":
        return rtsFiles
    else:
        pass
    for strPa, dummy_dirs, ltFiles in os.walk(unicode(strPath)):
        if strPa == STR_BASE_PATH:
            pass
        for strFile in ltFiles:
            if not strFile.endswith(ltExtensions):
                continue
            else:
                rtsFiles.append(os.path.join(strPath, strFile))
    return rtsFiles




if __name__ == '__main__':
    print fileCrawler('C:\\Users\\wang\\workspace\\')