from django.urls import path
from shop.views import index,  indexItem, addItem

app_name = "shop"

urlpatterns = [
    path("", index),
    path("<int:product_id>/", indexItem, name = "detail"),
    path("additem/", addItem, name = "add_item"),
    
    
]
