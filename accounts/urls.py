from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login_user/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("add/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('order/add/', views.add_to_order, name='add_to_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

]