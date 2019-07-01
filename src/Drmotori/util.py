from django.db.models import Min, Max
from hashlib import md5

from shop.models import Product

import smtplib
import ssl


def get_min_good_price():
    Product.objects.filter().value_list('Price').annotate(Min('Price')).order_by('price')[0]


def get_max_good_price():
    Product.objects.filter().value_list('Price').annotate(Max('Price')).order_by('price')[0]


def string_to_md5(input_str):
    return md5(input_str.encode('utf-8')).hexdigest()


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
