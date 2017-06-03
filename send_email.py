import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess


ipaddy = subprocess.check_output(['curl', 'v4.ifconfig.co'])

gmail_user = 'me@gmail.com'  
gmail_password = 'password'

fromaddr = "me@gmail.com"
toaddr = "you@gmail.com"

#m = email.message.Message()
msg = MIMEText("Good Morning!\n\nIP: %s" % (ipaddy))
msg['Subject'] = "Send mail from python!!"
msg['From'] = "Mr. Robot"
msg['To'] = "Mrs. Robot"


try:  
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(fromaddr, toaddr, msg.as_string())
	server.quit()
	print ('Email sent!')

except:  
    print ('Something went wrong...')
