from django.db.models import Min, Max

from .models import Good


def get_min_good_price():
    Good.objects.filter().value_list('Price').annotate(Min('Price')).order_by('price')[0]


def get_max_good_price():
    Good.objects.filter().value_list('Price').annotate(Max('Price')).order_by('price')[0]
