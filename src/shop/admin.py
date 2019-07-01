from django.contrib import admin

from .models import Product, Image, Color, Category, Tag, Basket, BasketLine, Commentor, Comment


admin.site.register(Product)
admin.site.register(Commentor)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Basket)
admin.site.register(BasketLine)
