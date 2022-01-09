from os import name
from django.contrib import admin
from django.conf.urls import include,url
from product import views
from product.middlewares.auth import auth_middleware

urlpatterns = [
    url('^$',views.Products.as_view(), name='homepage'),
    url('signup', views.Signup.as_view(), name='signup'),
    url('login', views.Login.as_view(), name='login'),
    url('logout', views.logout, name='logout'),
    url('cart', views.Cart.as_view(), name='cart'),
    url('check-out', views.CheckOut.as_view(), name='checkout'),
    url('orders', auth_middleware(views.Orders.as_view()), name='orders'),
    #url('^$',index),
    # url('create/',views.Customers.as_view()),
    # url('^update/address/(?P<addressId>[1-9]+)$',views.UpdateAddress.as_view()),
    # url('^details/(?P<accountnumber>[1-9]+)$',views.AccountDetails.as_view()),
    # #url('login/',views.CustomerLogin.as_view()),
]