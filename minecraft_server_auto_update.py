#import requests
#import sys
import os
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
    siteUrl = "https://minecraft.net/en-us/download/server/"
    serverVersion = CheckLatestServerVersion(siteUrl)
    versionStatus = 1
    if serverVersion != 1:
        versionStatus = comparePreviousVersion(serverVersion, filename)
    else:
        exit()

    if versionStatus != 1:
        overwriteFile(filename, serverVersion)
        serverUrl = getServerUrl(siteUrl)
        Message = upgradeMinecraft(serverUrl)
        sendEmail(Message)
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




def CheckLatestServerVersion(siteUrl):
    url = siteUrl
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


def getServerUrl(siteUrl):
    url = siteUrl
    urlData = urlopen(url)
    pageContent = urlData.read()
    urlData.close()

    soup = BeautifulSoup(pageContent, "html.parser")
    for item in soup.find_all(attrs={'class': 'col-12 col-md-10 col-lg-8'}):
        for link in item.find_all('a'):
            x = re.findall("server.jar", str(link))
            if len(x) != 0:
                return link.get('href')
    return 0


def upgradeMinecraft():
    stopStatus = stopMinecraftService()
    if stopStatus != 0:
        stopStatusError = ["Error: Unable to stop minecraft-server.service"]
        return stopStatusError

    updateStatus, updateLog = updateMinecraftServer()
    if updateStatus != 0:
        return updateLog

    startStatus = startMinecraftService()
    if startStatus != 0:
        startStatusError = ["Error: Unable to start minecraft-server.service"]
        return startStatusError

    SuccessMessage = ["Hooray! Your Minecraft Server located at <ip> has been updated! Please enjoy responsibly"]
    return SuccessMessage


def stopMinecraftService():
    ServiceStatus = os.system("systemctl stop minecraft-server.service")
    return ServiceStatus


def startMinecraftService():
    ServiceStatus = os.system("systemctl start minecraft-server.service")
    return ServiceStatus


def updateMinecraftServer(serverUrl):
    updateStatus = 1
    updateLog = []

    downloadServer = os.system("wget {} /opt/minecraft-stage/server.jar".format(serverUrl))
    if downloadServer != 0:
        updateLog.append("Error: Unable to download latest minecraft server.")
        updateLog.append("URL: {}".format(serverUrl))
        return updateLog
    removeOldVersion = os.system("rm /opt/minecraft-previous/server.jar")
    if removeOldVersion != 0:
        updateLog.append("Error: Unable to delete previous server.jar file from /opt/minecraft-previous/")
    backupCurrentVersion = os.system("mv /opt/minecraft/server.jar /opt/minecraft-previous/")
    if backupCurrentVersion != 0:
        updateLog.append("Error: Unable to backup server.jar from /opt/minecraft/ to /opt/minecraft-previous/")
    addNewVersion = os.system("mv /opt/minecraft-stage/server.jar /opt/minecraft/")
    if addNewVersion == 0:
        updateStatus = 0
        updateLog.append("Success: Moved new server.jar file to /opt/minecraft/")
    else:
        updateLog.append("Error: Unable to move new server.jar file to /opt/minecraft/")

    return updateStatus, updateLog


def sendEmail(Message):
    embody = Message

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
