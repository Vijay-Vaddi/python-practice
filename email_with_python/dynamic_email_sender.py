import smtplib
from email.message import EmailMessage
from pathlib import Path #to get access to outside files like .html etc
from string import Template #to give input to data using $ operators


html = Template(Path('index.html').read_text()) 
#to read it as a text
#wrap it in Template to make the variable custom in html files. 

email = EmailMessage()
email['from'] = 'Vijay Vaddi'
email['to'] = 'vijaykvaddi@gmail.com'
email['subject'] = 'Just keep going'

# email.set_content('You know it\'ll work if you keep going so keep going my brother')
#have to tell it the set content is in HTML, so set content =html in 2nd parameter

email.set_content(html.substitute({'name':'Vijay Vaddi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vijayzvaddi@gmail.com', 'iktabceccqirkpuc')
    smtp.send_message(email)
    print('Message sent')