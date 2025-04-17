from django.shortcuts import render, get_object_or_404

from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product/list.html', {'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, "shop/product/detail.html", {"product": product})