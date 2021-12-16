import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('dummysakti@gmail.com', 'Dumm#sak1')
server.sendmail('dummysakti@gmail.com', 'hisakti@gmail.com', 'testig message')

server.quit()

# from email.message import EmailMessage

# email = EmailMessage()
# email['from'] = 'dummysakti@gmail.com'
# email['to'] = 'hisakti@gmail.com'
# email['subject'] = 'Sample email test from python!'

# email.set_content('I am a Python Master!')

# with smtplib.SMTP(host='smtp.gmail.com', port=578) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('dummysakti@gmail.com', 'Dumm#sak1')
#     smtp.send_message(email)
#     print('all good boss!')
