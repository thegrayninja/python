import sys
import csv
from collections import defaultdict


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


def main():
    CheckPythonVersion()
    SpecialCharacters = "`!@#$%^&*()=+|'\" "

    GetAppNameText = "Please enter the app name (default: crowdstrike): "
    GetCSVFilenameText = "Please enter CSV filename (default: crowdstrike.csv): "
    app_name = GetAppName(SpecialCharacters, GetAppNameText)
    csv_filename = GetAppName(SpecialCharacters, GetCSVFilenameText)

    if app_name == "":
        app_name = "crowdstrike"

    if csv_filename == "":
        csv_filename = "crowdstrike.csv"


    columns = defaultdict(list) # each value in each column is appended to a list

    with open(csv_filename) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                columns[k].append(v) # append the value into the appropriate list
                                     # based on column name k

    CSHostData = ""
    AppFilename = "{}_hostnames.txt".format(app_name)
    try:
        with open(AppFilename, 'w') as CSHosts:
            for i in columns['Host Name']:
                if i.strip() != " ":
                    CSHostData += "{}\n".format(i.strip())
            CSHosts.write(CSHostData)
    except:
        print("Error creating file: '{}'".format(AppFilename))

    print("Data saved to .\\{}".format((AppFilename)))


if __name__ == main():
    main()