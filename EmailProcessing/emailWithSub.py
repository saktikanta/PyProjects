import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'Sakti'
msg['To'] = 'hisakti@gmail.com'
msg['Subject'] = 'Sample email test from python!'

msg.set_content('I am a Python Master!')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('dummysakti@gmail.com', 'Dumm#sak1')
server.send_message(msg)
server.quit()

# with smtplib.SMTP(host='smtp.gmail.com', port=578) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('dummysakti@gmail.com', 'Dumm#sak1')
#     smtp.send_message(msg)
#     print('all good boss!')
