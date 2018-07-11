import sys



def main():
    CheckPythonVersion()
    SpecialCharacters = "`!@#$%^&*()=+|'\" "

    GetAppNameText = "Please enter the app name (default: crowdstrike): "
    GetFilenameText = "Please enter app inventory list (default: .\crowdstrike_hostnames.txt): "
    GetMasterFilenameText = "Please enter os inventory list (default: .\windows_servers.txt): "

    app_name = GetAppName(SpecialCharacters, GetAppNameText)
    app_filename = GetAppName(SpecialCharacters, GetFilenameText)
    master_filename = GetAppName(SpecialCharacters, GetMasterFilenameText)

    if app_name == "":
        app_name = "crowdstrike"

    if app_filename == "":
        app_filename = ".\crowdstrike_hostnames.txt"

    if master_filename == "":
        master_filename = ".\windows_servers.txt"


    with open(app_filename) as AppFile:
        AppData = AppFile.readlines()

    with open(master_filename) as MasterFile:
        MasterData = MasterFile.readlines()



    DataResults = CompareLists(AppData, MasterData)


    InAppFilename = app_name + "_contains.txt"
    NotInAppFilename = app_name + "_missing.txt"
    SaveDataToFiles(InAppFilename, DataResults[0])
    SaveDataToFiles(NotInAppFilename, DataResults[1])

    print("\nall done. check .\\{} AND {} for results".format(InAppFilename, NotInAppFilename))



def CheckPythonVersion():
    PyVerTuple = sys.version_info[:1]
    if PyVerTuple[0] > 2:
        return 0
    else:
        print("\n\nPlease run Python 3.x or newer\n")
        sys.exit(1)


def GetAppName(SpecialCharacters, StringToAsk):
    UserInput = input(StringToAsk)
    for Character in SpecialCharacters:
        if Character in UserInput:
            print("\nERROR! '{}' character is not allowed. Please try again.\n")
            GetAppName(SpecialCharacters)
    return UserInput


def SaveDataToFiles(Filename, Data):
    UpdatedData = ""
    for host in Data:
        UpdatedData += "{}\n".format(host.strip())
    with open(Filename, "w") as ServerFile:
        ServerFile.write(UpdatedData)


def CompareLists(AppData, MasterData):
    Counter = 0
    TotalInApp = 0
    TotalNotInApp = 0
    HostsInApp = []
    HostsNotInApp = []
    for MasterHostname in MasterData:
        if MasterHostname in AppData:
            HostsInApp.append(MasterHostname)
            TotalInApp += 1
        else:
            HostsNotInApp.append(MasterHostname)
            TotalNotInApp += 1

        Counter += 1


    print("Total hosts in app: {}".format(TotalInApp))
    print("Total hosts not in app: {}".format(TotalNotInApp))
    print("Total hosts: {}".format(Counter))
    ReturnData = (HostsInApp, HostsNotInApp)
    return ReturnData







if __name__ == main():
    main()

