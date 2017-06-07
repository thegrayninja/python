##github.com/grayninja
##e-mail my wife the weather report

import json
import requests
import time


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess


url = 'https://api.weather.gov/points/121.0109,-78.1002/forecast'
forecast = requests.get(url)

tempFile = open("save_weather.json", "w")
tempFile.write(forecast.content)
tempFile.close()


####
####PARSE JSON
####

originalFile = "save_weather.json"
with open (originalFile, "r") as data_file:
	counter = 0
	results = "7 day Forecast:\n\n"
	agent_scanned = ""
	data = json.load(data_file)
	for i in (data["properties"]["periods"]):
		tod = (data["properties"]["periods"][counter]["name"]) #tod == time of day
		startTime = (data["properties"]["periods"][counter]["startTime"])
		detailedForecast = (data["properties"]["periods"][counter]["detailedForecast"])
		counter += 1
		results += ("%s\t%s\n\n" % (tod, detailedForecast))

####
####END PARSE JSON
####




####
####SEND E-MAIL
####
sign_off = "\n\nI Love you!!"
gmail_user = 'email@gmail.com'  
gmail_password = 'password'

fromaddr = "email@gmail.com"
toaddr = "email@gmail.com"


msg = MIMEText("%s%s" % (results,sign_off))
msg['Subject'] = "Weather Forecast"
msg['From'] = "The Weather Man"
msg['To'] = "Wifey"


try:  
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(fromaddr, toaddr, msg.as_string())
	server.quit()
	print ('Email sent!')

except:  
    print ('Something went wrong...')


####
####END OF SEND E-MAIL
####
