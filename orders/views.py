from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    
    # Предзаполнение формы данными авторизованного пользователя
    initial_data = {}
    if request.user.is_authenticated:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
    
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
          
            cart.clear()      
           
            return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm(initial=initial_data)
    
    return render(request, "orders/order/create.html", {
        "cart": cart, 
        "form": form,
        "user": request.user
    })
