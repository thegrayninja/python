#import requests
#import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


# import related to email...or can use aws notifications
import smtplib
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#import os
#import subprocess
from smtp_stats import gmail_password, gmail_user, toaddr, fromaddr


def main():
    print("thanks for turning me on")
    filename = "minecraft_server_version.txt"
    serverVersion = CheckLatestServerVersion()
    versionStatus = 1
    if serverVersion != 1:
        versionStatus = comparePreviousVersion(serverVersion, filename)
    else:
        exit()

    if versionStatus != 1:
        overwriteFile(filename, serverVersion)
        sendEmail()
        # TODO alert admin if values are different
    else:
        print("nothing to do. versions match.")

    print("i hope you are satisfied")


def openFileRead(filename):
    with open(filename, "r") as newfile:
        dataInFile = newfile.read()
    return dataInFile

def overwriteFile(filename, serverVersion):
    try:
        with open(filename, "w") as newfile:
            newfile.write(serverVersion)
        print("new server version saved successfully")
    except Exception as e:
        print(e)
        exit()




def CheckLatestServerVersion():
    url = "https://minecraft.net/en-us/download/server/"
    urlData = urlopen(url)
    pageContent = urlData.read()
    urlData.close()

    soup = BeautifulSoup(pageContent, "html.parser")

    for i in soup.find_all('code'):
        x = re.findall("minecraft_server.*.jar", str(i))
        if len(x) == 0:
            #print("it's blank")
            return 0
        else:
            serverVersion = ''.join(x)
            #print(''.join(x))
            return serverVersion
    return 1

def comparePreviousVersion(serverVersion, filename):
    currentVersion = openFileRead(filename).strip()
    print(currentVersion)
    if serverVersion == currentVersion:
        print("versions match!")
        return 1
    else:
        print("Version {} is now available!".format(serverVersion))
        return serverVersion



def sendEmail():
    embody = "\nThe latest version of Minecraft Server - Java Edition has been released\n\nPlease download it now so your kids don't fight.\n"

    sign_off = "\n\nYou're Welcome.\n"

    msg = MIMEText("{}{}".format(embody, sign_off))
    msg['Subject'] = "New Minecraft Version Available"
    msg['From'] = "Trent"
    msg['To'] = "G-Man"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

if __name__ == "__main__":
    main()
