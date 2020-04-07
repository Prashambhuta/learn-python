#! usr/bin/env python3

"""
Checking emails using the module for IMAP: imaplib

We will use 3rd party modules:
1. imapclient - for fetching emails
2. pyzmail - for parsing
"""

# import imapclient & pyzmail
import imapclient, pyzmail
import dotenv, os

# loading the env variables
dotenv.load_dotenv()

# create a connection object
conn_object = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# call the login method
conn_object.login('prasham.bhuta', os.getenv('my_password'))

# select the INBOX folder
conn_object.select_folder('INBOX', readonly=True)

# searching for emails
mails_to_me = conn_object.search(["FROM", "prasham.bhuta@gmail.com"])
print(mails_to_me)

# fetching the required email
req_email = conn_object.fetch([66304], 'BODY[]')
print(req_email)

# parsing with pyzmail message object
email_message = pyzmail.PyzMessage.factory(req_email[66304][b'BODY[]'])

# printing required fields
print(email_message.get_subject())
print(email_message.get_addresses('bcc'))

# check for 'text' and 'html' part of email
print(email_message.text_part)
print(email_message.html_part)

# get the main part of the email
main_text = email_message.text_part.get_payload().decode('UTF-8')
print(main_text)

# searching for a particular text
text = "IELTS"
email_with_text = conn_object.search('TEXT "%s"' % text)
print(email_with_text)
text_email = conn_object.fetch([66362], 'BODY[]')
print(text_email)
message_in_text_email = pyzmail.PyzMessage.factory(text_email[66362][b'BODY['
                                                                     b']'])
main_text = message_in_text_email.text_part.get_payload().decode('UTF-8')
print(main_text)

# using other folders
print(conn_object.list_folders())

# delete emails
conn_object.select_folder("INBOX", readonly=False)
todays_email = conn_object.search('ON 06-Apr-2020')
print(todays_email)
# conn_object.delete_messages([email_number])



# to finish and logout
conn_object.logout()


