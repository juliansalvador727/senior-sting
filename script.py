import smtplib
import pandas as pd
from email.mime.text import MIMEText

#email subject
subject = "Senior Sting"
#your email
sender = "..."

#change name path
spreadsheet = pd.read_excel('C:/Users/.../sting.xlsx')

#cc / bcc
recipients = ["..."]
password = "..."

emails = spreadsheet['EMAIL']
names = spreadsheet['NAME']
targets = spreadsheet['TARGET']

#send emails
for x in range(len(emails)):
    email = emails[x]
    name = names[x]
    target = targets[x]
    body = "Hello "+name+",\nYour senior sting target is " + target + "\n\nGood Luck!\nJulian S."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, email, msg.as_string())
    print("Message sent!")