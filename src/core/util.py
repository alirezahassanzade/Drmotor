from django.db.models import Min, Max

from .models import Good, Good_Image, Image


def get_min_good_price():
    Good.objects.filter().value_list('Price').annotate(Min('Price')).order_by('price')[0]


def get_max_good_price():
    Good.objects.filter().value_list('Price').annotate(Max('Price')).order_by('price')[0]


def get_first_good_pic(good_id):
    good = Good.objects.filter(id=good_id)[0]
    good_image = Good_Image.objects.filter(Good=good)
    if len(good_image) >= 1:
        return good_image[0].Image.Img.url
    else:
        return '/static/img/nopic.png'
