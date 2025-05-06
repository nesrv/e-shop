## инет магазин 2

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
python manage.py createsuperuser
```

```
при оформлении заказа order create нужно в html подставить данные о пользователе, которые авторизован в данный момент на сайте

```


```py
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
    

```


```html
{% block content %}
  <h1>Checkout</h1>
  
  {% if user.is_authenticated %}
  <div class="user-info">
    <p>Оформление заказа для: <strong>{{ user.username }}</strong></p>
  </div>
  {% endif %}

```


```py
last_name = models.CharField(max_length=50, blank=True, null=True)
```

```shell
python manage.py makemigrations
python manage.py migrate
```


# Интернационализация

```shell
pip install django-rosetta
```

```py
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
```


```py
    'django.middleware.locale.LocaleMiddleware',  # Добавлен middleware для локализации

```


```py

rom django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


# URL-шаблоны, не требующие перевода
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
]

# URL-шаблоны, требующие перевода
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),
    prefix_default_language=True,
)

```

дальше меняем base.html