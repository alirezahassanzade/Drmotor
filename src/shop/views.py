from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from shop.models import Product, Basket, BasketLine, Comment
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView


def shop_view(request):
    # '/static/img/nopic.png'
    goods_list = Product.objects.all()
    context = {
        'goods_list': goods_list,
    }
    return render(request, 'shop/home.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product=self.object).filter(approved=True)
        return context


def add_to_basket(request):
    product = get_object_or_404(Product, pk=request.GET.get("product_id"))
    basket = request.basket
    if not request.basket:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        basket = Basket.objects.create(user=user)
        request.session["basket_id"] = basket.id

    basketline, created = BasketLine.objects.get_or_create(basket=basket, product=product)
    if not created:
        basketline.quantity += 1
        basketline.save()
    return HttpResponseRedirect(reverse("product", args=(product.slug,)))
