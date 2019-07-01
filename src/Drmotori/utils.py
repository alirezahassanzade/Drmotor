from django.utils.text import slugify
import random
import string

import smtplib
import ssl


def send_mail(message_detail):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "dr.motori.start@gmail.com"
    receiver_email = "dr.motori.start@gmail.com"
    password = "sh@@rbaf2211nickipedram"
    message = ''.join("""\
    Subject: Hi

    You have a new request!
    Details are as follows:
    """ + message_detail).encode('utf-8').strip()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    class_ = instance.__class__
    qs_exists = class_.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=5)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
