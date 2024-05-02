from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', vendors),
    path('vendors/<int:vendor_id>/', vendor_detail),
]
