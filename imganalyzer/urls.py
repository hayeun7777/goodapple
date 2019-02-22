from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'imganalyzer'

urlpatterns = [
    path('', views.index),
    path('home', views.home, name='home'),
    path('result', views.result, name='result'),
    path('details', views.details, name='details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)