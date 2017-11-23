ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "janez.kovac77" + ORG_EMAIL
FROM_PWD = "janez.kovac.1960"
TO_EMAIL = "janez.kovac77@gmail.com"
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

SMTP_SERVER =  "smtp.gmail.com"
SMTP_PORT = 587

import smtplib
import time
import imaplib
import email


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        for i in range(latest_email_id, first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    #msg = email.message_from_string(response_part[1]).decode['utf-8']
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))

def send_email_from_gmail(emailText):
    try:
        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, FROM_PWD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, emailText)
        server.quit()
    except Exception as e:
        print(str(e))


read_email_from_gmail()

msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])

send_email_from_gmail(msg)