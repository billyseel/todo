from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('update/<str:pk>', update, name="update"),
    path('delete/<str:pk>', delete, name="delete"),
    # path('products/', products),
    # path('contact/', contact),
    # path('update/<str:pk>', update)
]
