#!/usr/bin/env python
# -*- coding:utf8 -*
# The Mozilla Public License 2.0 (MPL 2.0)

# Copyright (c) 2015 Zhichao Wang

# This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this
#   file, You can obtain one at http://mozilla.org/MPL/2.0/.
# 
# If it is not possible or desirable to put the notice in a particular
# file, then You may include the notice in a location (such as a LICENSE
# file in a relevant directory) where a recipient would be likely to look
# for such a notice.
# 
# You may add additional accurate notices of copyright ownership.
#

"""
.. Use Python to crack Zip encrypted files with password dictionary files. 
.. The project is created to understand Python's multi threading programming.
"""

__author__ = 'zhichao,wang'
__email__ = 'ziccowarn@gmail.com'
__url__ = 'http://www.me-lot.com/'
__version__ = '0.1'
__license__ = 'MPL 2.0'
__status__ = 'Beta'
__revision__ = '$Rev: 01 $'
__updated__ = '2018-07-16'


import zipfile
import os
import optparse
from threading import Thread
import Queue
STR_BASE_PATH, STR_MODULE_NAME = os.path.split(__file__)


class MY_NO_MATCH(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr("PASSWORD [NO MATCH]: " + str(self.value))

class MY_YES_MATCH(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr("PASSWORD [MATCHED]: " + str(self.value))


def extractFile(zFile, password, bucket):
    try:
        zFile.extractall(pwd=password.encode(encoding="utf-8"))
        bucket.put(MY_YES_MATCH(password))
    except:
        bucket.put(MY_NO_MATCH(password))
        
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
 
def main():
    parse = optparse.OptionParser("useage%prog " + "-f <zipfile> -d <dictionary>/-r <dictionary folder>")
    parse.add_option("-f", dest="zname", type="string", help="specify zip file")
    parse.add_option("-r", dest="rname", type="string", help="specify dictionary folder")
    parse.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    (options, args) = parse.parse_args()  # @UnusedVariable
    if (options.zname is None) or (options.dname is None and options.rname is None) :
        print parse.usage
    else:
        zname = options.zname
        dname = options.dname
        rname = options.rname
        if dname:
            zFile = zipfile.ZipFile(zname)
            passFile = open(dname)
            for line in passFile.readlines():
                password = line.strip("\n")
                t = Thread(target=extractFile, args=(zFile, password))
                t.start()
        elif rname:
            bucket = Queue.Queue()
            zFile = zipfile.ZipFile(zname)
            ltFiles = fileCrawler(rname)
            if not ltFiles:
                print parse.usage
                return
            for pwFile in ltFiles:
                passFile = open(pwFile)
                for line in passFile.readlines():
                    password = line.strip("\n")
                    t = Thread(target=extractFile, args=(zFile, password, bucket))
                    t.start()
                    while True:
                        try:
                            exc = bucket.get(block=False)
                        except Queue.Empty:
                            pass
                        else:
                            if isinstance(exc, MY_YES_MATCH):
                                print exc
                                return
                            elif isinstance(exc, MY_NO_MATCH):
                                print exc
                                break
                        t.join(0.1)
                        if t.isAlive():
                            continue
                        else:
                            break
        else:
            print parse.usage

if __name__ == "__main__":
    main()
