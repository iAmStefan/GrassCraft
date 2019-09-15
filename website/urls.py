from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informatii/', views.informations, name='informatii'),
    path('regulament/', views.rules, name='regulament'),
    path('modele-cereri/', views.staffRequests, name='staffRequests'),
    path('voteaza/', views.vote, name='vote'),
    path('404/', views.error404, name='error'),
]
