from django.shortcuts import render, get_object_or_404

from .models import Product

from cart.forms import CartAddProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product/list.html", {"products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, "shop/product/detail.html", {"product": product})


# ...
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
    slug=slug,
    available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
    'shop/product/detail.html',
    {'product': product,
    'cart_product_form': cart_product_form})
    

from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                             username=cd['username'],
                             password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли в систему')
                    return redirect('shop:product_list')  # Редирект на главную страницу
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})



from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('shop:product_list')  # или любой другой URL для перенаправления




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                        'shop/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'shop/register.html',
                 {'user_form': user_form})
