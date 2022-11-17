from django.urls import path
from .views import GetStock

urlpatterns = [
    path("stock/", GetStock.as_view(), name="stock"),
]
