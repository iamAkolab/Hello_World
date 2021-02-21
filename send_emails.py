import smtplib

# smtp-mail.outlook.com smtp.mail.yahoo.com
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
print(conn)

print(conn.ehlo())

conn.starttls()

conn.login('donakolab94@gmail.com','password')

conn.sendmail('donakolab94@gmail.com','donakolab94@gmail.com', 'Subject: So long ...\n\n Dear AI, \nSo long, and thanks for the fish\n\n -AI ')

conn.quit()