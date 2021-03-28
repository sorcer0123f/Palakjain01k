import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "iampalakjain01@gmail.com"  # Enter your address
receiver_email = "itspalak19@gmail.com"  # Enter receiver address
password = "xecbeupbulzfwpos"
message = """\
Subject: Error!
Hey,
you have some error on your HTML website
Please check !
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)