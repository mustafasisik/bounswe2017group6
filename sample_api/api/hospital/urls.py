from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^doctor/$', views.doctor, name='doctor'),
    url(r'^doctor/([0-9]+)/$', views.doctor_single, name='doctor'),
]
