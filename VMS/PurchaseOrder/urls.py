from django.urls import path
from .views import *

urlpatterns = [
    path('api/purchase_orders/<int:po_id>/', purchase_order_detail),
    path('api/purchase_orders/', purchase_order),
]
