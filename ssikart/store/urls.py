"""
URL configuration for ssikart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from store.views import product_detail,shop,store_home

urlpatterns = [
    path("",shop,name="ssi-store-shop"),
    path("product_details",store_home,name="ssi-store-home"),
    path('<slug:category_slug>', shop, name='ssi-store-shop'),
    path('<slug:category_slug>/<slug:product_slug>', product_detail, name='ssi-store-home'),
    # path("about",about,name="ssi-about"),
    # path("checkout",checkout,name="ssi-checkout")
]
