from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informatii/', views.informations, name='informatii'),
    path('regulament/', views.rules, name='regulament'),
    path('cereri-staff/', views.staffRequests, name='staffRequests'),
    path('404/', views.error404, name='eroare'),
    path('cereri-staff/', views.sendmail, name='sendmail'),
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        ('static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
