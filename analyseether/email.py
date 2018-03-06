from flask_mail import Message
from analyseether import app, mailgun


def send_email(to, subject, template):
    message = Message()
    message.subject = subject
    message.recipients = [to]
    message.sender = app.config['MAIL_DEFAULT_SENDER']
    message.html = template

    mailgun.send(message)
    print "email sent"
