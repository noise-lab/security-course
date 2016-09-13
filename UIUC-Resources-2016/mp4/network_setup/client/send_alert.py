#!/usr/bin/python
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib, sys

issue = sys.argv[1]
username = 'cs461.alert'
password = 'cS46!eCE42@alerT!'
sender = 'cs461.alert@gmail.com'
msg = MIMEMultipart()
msg["Subject"] = "MP4 Alert"
msg["From"] = "cs461.alert@gmail.com"
msg["To"] = "skim104@illinois.edu"
body = MIMEText(issue)
msg.attach(body)
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
server.quit()
print "Alert email sent."
