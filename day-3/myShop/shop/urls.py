from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'shop'

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('login/', views.user_login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
