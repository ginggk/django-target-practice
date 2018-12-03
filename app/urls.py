from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name='double'),
    path('multiple/', views.Multiple.as_view(), name='multiple'),
    path('earnings/', views.Earnings.as_view(), name='earnings'),
    path('both/', views.Both.as_view(), name='both'),
    path('walkordrive/', views.walkOrDrive.as_view(), name='walkordrive'),
    path('populated/', views.HowPopulated.as_view(), name='populated'),
    path('stars/', views.Stars.as_view(), name='stars'),
    path('points/', views.Points.as_view(), name='points')
]
