from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informatii/', views.informations, name='informatii'),
    path('regulament/', views.rules, name='regulament'),
    path('cereri-staff/', views.staffRequests, name='staffRequests'),
    path('cereri-staff/', views.sendmail, name='sendmail'),
]

handler404 = 'views.handler404'
