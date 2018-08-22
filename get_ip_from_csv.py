#I had to extract column 0 from over 20 separate .csv files
#They all lived in the same directory, so i wrote this script
#  which reads all column 0 values from all .csv files.
#The script will only import .csv files. You can modify this
#  "feature" in def LoadFile(), then modify "FileName.endswith(".csv")
#Tested on Windows 10 via python3

__author__ = "grayninja"
__version__ = "1.0"
__compatibility__ = "Windows 10"

import csv
import os

print("\n{}\n{}\n{}\n\n".format(__author__, __version__, __compatibility__))
DocContents = []

#if encoding is required, replace with this line:
#with open('.\\files\workbook2.csv', 'rt', encoding='utf8') as csvfile:


def main():
    FileNames = GetFileName()
    IPs = LoadFile(FileNames)
    SaveData(IPs)
    print("done")


def GetFileName():
    ListOfFiles = os.listdir(".\\SubnetExport\\")
    return ListOfFiles


def LoadFile(FileNames):
    DocContents = []
    MasterIPList = ""
    for FileName in FileNames:
        if FileName.endswith(".csv"):
            FullFileName = ".\\SubnetExport\\{}".format(FileName)
            with open(FullFileName, 'rt') as csvfile:
                CSVData = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in CSVData:
                    DocContents.append(row)
    MasterIPList += ParseData(DocContents)

    return MasterIPList


def ParseData(CSVData):
    Count = 0
    IPAddresses = ""
    for row in CSVData:
        IPAddress = ""
        for IPChar in CSVData[Count][0]:
            IPAddress += IPChar     # IPChar is a single character, thus the need to combine
        if IPAddress != "IP Address":   # IP Address is the header value in Column 0
            IPAddresses += "{}\n".format(IPAddress)
        Count += 1

    return IPAddresses

def SaveData(Data):
    with open("master_ip_list.txt", "w") as MasterFile:
        MasterFile.write(Data)





if __name__ == main():
    main()
#print("whoops")

