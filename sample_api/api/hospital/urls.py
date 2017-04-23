from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^doctor/$', views.doctor, name='doctor'),
    url(r'^doctor/([0-9]+)/$', views.doctor_single, name='doctor_single'),
    url(r'^patient/([0-9]+)/$', views.patient_single, name='patient_single'),
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^department/$', views.department, name = 'department'),
    url(r'^department/([0-9]+)/$', views.department_single, name = 'department_single'),
]
