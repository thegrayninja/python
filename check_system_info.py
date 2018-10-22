#source: https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python

import psutil
import os
from subprocess import check_output
import sys


def main():

    ProcessName, LengthInSeconds = ProcessArguments()
    GetInfoOfSeparateTask(ProcessName, int(LengthInSeconds))


def HelpMenu():
    HelpText = """

Usage:
    python3 check_system_info.py -p chrome -t 4
    
    
switches:
    -t    total length in time to run and gather system average
    -p    name of process. Refer to 'top' as necessary
    
        
"""
    print(HelpText)
    sys.exit(0)


def ProcessArguments():
    ProcessName = "Xorg"
    LengthInSeconds = "10"

    Arguments = sys.argv
    if len(Arguments) > 1:
        Counter = 1
        while Counter < len(Arguments):
            if Arguments[Counter] == "-p":
                try:
                    ProcessName = Arguments[(Counter+1)]
                except:
                    print("error - missing process name")
                    HelpMenu()
            if Arguments[Counter] == "-t":
                try:
                    LengthInSeconds = Arguments[(Counter+1)]
                except:
                    print("error - missing length in seconds")
                    HelpMenu()
            #print(Arguments[Counter])
            Counter += 1
    return ProcessName, LengthInSeconds






    ArgLength = len(sys.argv)


def GetInfoOfCurrentTask():
    pid = os.getpid()
    py = psutil.Process(pid)
    CPUUsage = py.cpu_percent(3)
    CPUUsage2 = py.cpu_times()
    MemoryUsage = py.memory_info()[0]/2.**30 #memory use in GB...
    print('memory use: {}\ncpu use: {}'.format(MemoryUsage, CPUUsage2))
    print('cpu percentage: {}'.format(py.cpu_percent(2)))
    #print(psutil.cpu_percent())
    print(psutil.virtual_memory())



def GetInfoOfSeparateTask(Name, LengthInSeconds):
    #PID = map(int, check_output(["pidof", Name]).split())
    PIDs = check_output(["pidof", Name]).split()
    ListOfPIDS = []
    for PID in PIDs:
        ListOfPIDS.append(PID.decode('utf-8'))

    print(ListOfPIDS)
    for i in ListOfPIDS:
        py = psutil.Process(int(i))
        #CPUUsage = py.cpu_times()
        KB = float(1024)
        GB = float(KB ** 3)

        py.cpu_percent(interval=None)
        py.memory_info()
        print(py.name())
        MemResults = []
        CPUResults = []
        for Time in range(LengthInSeconds):
            CPUUsage = py.cpu_percent(interval=1)
            MemoryVirtual = (py.memory_info()[0] >> 20)/1024
            #MemoryVirtualBits = py.memory_info()[1]
            #MemoryVirtualGigs = MemoryVirtualBits.total >> 30 # /GB
            #MemoryUsage = (py.memory_info()[1]/1024)/1024/1024/1024
            MemResults.append(MemoryVirtual)
            CPUResults.append(CPUUsage)
            #print(CPUUsage, MemoryVirtual)

        MemoryUsage = py.memory_info()[0]/2.**30
        #print('memory use: {} GB\ncpu percentage: {}'.format(MemoryUsage, CPUUsage))
        CPUAverage = sum(CPUResults)/float(len(CPUResults))
        MemoryAverage = sum(MemResults)/float(len(MemResults))

        print('\naverage:\nmemory use: {} GB\ncpu percentage: {}'.format(MemoryAverage, CPUAverage))





if __name__ == '__main__':
    #GetInfoOfSeparateTask("chrome", 2)
    main()




