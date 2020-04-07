#! usr/bin/env python3

"""
Sending automated email using 'smtplib' module
"""

import smtplib
import dotenv
import os

dotenv.load_dotenv()

# create a connection object which connects to a smtp server for sending &
# receiving email.
connection_object = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# connect to the server
connection_object.ehlo()

# start `tls` encryption
# connection_object.starttls()

# login to the account
# in gmail settings - TURN OFF TWO STEP VERIFICATION
#                   - TURN ACCESS TO LESS SECURE APP ON
connection_object.login('prasham.bhuta@gmail.com', os.getenv('my_password'))

# sending email
connection_object.sendmail(from_addr='prasham.bhuta@gmail.com',
                           to_addrs='prasham.bhuta@gmail.com', msg=
                           "Subject: My first email from python script "
                           "\n\nDear Prasham, \n great work with the python "
                           "script\n\nPrasham")

# disconnect from the smtp server
connection_object.quit()
