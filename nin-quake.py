import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import subprocess


embody = "\nNine Inch Nails - Quake Vinyl is Available!\n\nGet off your ass and buy it today: https://store.nin.com/collections/music/products/quake-ost-1xlp-1\n"

sign_off = "\n\nYou're Welcome.\n"
gmail_user = 'user@gmail.com'  
gmail_password = ''

fromaddr = "user@gmail.com"
toaddr = "user@gmail.com"


msg = MIMEText("%s%s" % (embody,sign_off))
msg['Subject'] = "NIN - Quake Vinyl"
msg['From'] = "Trent"
msg['To'] = "G-Man"


os.system('curl https://store.nin.com/collections/music/products/quake-ost-1xlp-1 > quake-ost.txt')
try:
	grep = subprocess.check_output(['grep', 'property="og:description" content="COMING SOON"', 'quake-ost.txt'])
	print(grep)  #simply for manual check

except:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(fromaddr, toaddr, msg.as_string())
	server.quit()

