from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("order/", views.order, name="order"),
    path("book_table/", views.order, name="book_table"),
    path("contact/", views.contact, name="contact"),
    path("menu/", views.menu, name="menu"),
    
]