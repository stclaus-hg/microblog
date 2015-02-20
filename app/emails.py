from threading import Thread
from app import mail, app
from app.decorators import async
import config
from flask import render_template
from flask.ext.mail import Message


@async
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
               config.ADMINS[0],
               [followed.email],
               render_template("follower_email.txt", user=followed, follower=follower),
               render_template("follower_email.html", user=followed, follower=follower)
               )
