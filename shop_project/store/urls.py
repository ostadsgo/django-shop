from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("store/<slug>/", views.product_info, name="product_info"),
]