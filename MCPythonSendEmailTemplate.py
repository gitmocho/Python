# Select 'Turn on' > https://www.google.com/settings/security/lesssecureapps

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Commencing')

# Specifying the from and to addresses
fromaddr = '<insert email address here>'
toaddrs  = '<insert email address here>'

# Gmail Login
username = '<insert email user name here>'
password = '<insert password here>'

# Writing the message (this message will appear in the email)
# msg = 'This email is sent via a Python program'
msg=MIMEMultipart()
msg['from']=fromaddr
msg['To']=toaddrs
msg['Subject'] = 'Test email - Did this work?'
body="This is the body of the email sent via a Python application."

msg.attach(MIMEText(body, 'plain'))
# Sending the mail  
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
print('Email successfully sent.')
server.quit()
