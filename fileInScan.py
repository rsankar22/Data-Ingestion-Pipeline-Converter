import os.path
from os import listdir
from os.path import isfile, join

def pullPath(inpt):
    mypath = inpt
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def pullFile(file):
    file_pull = os.path.basename(file)
    return file_pull
