from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Index'),
    path('about/',views.about, name='Abpot'),
    path('contact/',views.contact, name='Contact'),
    path('tracker',views.tracker, name='TrackingStatus'),
    path('search',views.search, name='Search'),
    path('productView',views.productView, name='Product'),
    path('checkout',views.checkout, name='Checkout')
]