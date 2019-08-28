from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informatii/', views.informations, name='informatii'),
    path('regulament/', views.rules, name='regulament'),
    path('cereri-staff/', views.staffRequests, name='staffRequests'),
    path('sendmail', views.sendmail, name='sendmail'),
    path('404/', views.error404, name='error'),
]
