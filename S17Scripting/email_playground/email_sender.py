# Email Sender

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Anastasia Olsen'
email['to'] = 'obrentpalmer@gmail.com'
email['subject'] = 'You won 1 000 000 dollars!'

email.set_content(html.substitute(name='Brent Palmer'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('anastasiaolsenn@gmail.com', 'vltysfuznvwclily')
	smtp.send_message(email)
	print("All good boss!")

