from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name='double')
]
