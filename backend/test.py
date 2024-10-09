import aiosmtplib
from email.message import EmailMessage
import asyncio

email = EmailMessage()
email['from'] = 'Kapi'
email['to'] = 'fediokamil@gmail.com'
email['subject'] = 'test lol'


email.set_content('<p>abc</p>')

async def mail():
    async with aiosmtplib.SMTP(hostname='smtp.gmail.com', port=587) as smtp:
        await smtp.login('kgx.dev@gmail.com', 'shzcqyvmafqvfdkd')
        await smtp.send_message(email)
        print('sent')

asyncio.run(mail())