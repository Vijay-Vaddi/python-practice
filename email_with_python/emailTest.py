import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Vijay Vaddi'
email['to'] = 'vijaykvaddi@gmail.com'
email['subject'] = 'Keep going my man'
email.set_content('Don\'t stop until you get it. You know it\'ll work.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vijayzvaddi@gmail.com', 'iktabceccqirkpuc')
    smtp.send_message(email)
    print('Message sent')
