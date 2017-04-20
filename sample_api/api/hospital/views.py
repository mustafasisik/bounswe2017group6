from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
@csrf_exempt
def doctor(request):
    if request.method == 'GET':
        return JsonResponse({"asd":"asd"})

@csrf_exempt
def doctor_single(request, doctor_id):
    if request.method == "GET":
        print(request)
        doctor = Doctor.objects.filter(id=int(doctor_id))
        if doctor.exists():
            doctor = doctor.first()
        return JsonResponse({"name":doctor.name, "lastname":doctor.lastname, "age":doctor.age})

    elif request.method == "POST":
        pass
