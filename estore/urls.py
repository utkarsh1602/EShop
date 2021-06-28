"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views.home import homepage
from home.views.list import topwearList,bottomwearList,accesoriesList
from home.views.register import Register,Login,Logout
from home.views.cartpage import Cart
from home.views.checkout import Checkout

from django.conf.urls import include, url
from payment.views import Home,success,failure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage.as_view()),
    path('list/topwear/',topwearList.as_view()),
    path('list/bottomwear/',bottomwearList.as_view()),
    path('list/accessories/',accesoriesList.as_view()),
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('cart/',Cart.as_view()),
    path('checkout/', Checkout.as_view()),

    path('checkout/payment',Home, name='payment'),
    url(r'^Success/',success),
    url(r'^Failure/',failure),
]
