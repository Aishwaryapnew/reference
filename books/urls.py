from django.urls import path
from . import views

urlpatterns = [
    path('references/', views.references, name='references'),
    path('references/reference_insert/', views.reference_insert, name='reference_insert'),
]