from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

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

@csrf_exempt
def patient_single(request, patient_id):
    if request.method == "GET":
        print(request)
        patient = Patient.objects.filter(id=int(patient_id))
        if patient.exists():
            patient = patient.first()
        else:
            pass
        return JsonResponse({"name":patient.name, "lastname":patient.lastname, "age":patient.age})
        
    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        patient = Patient.objects.filter(id=int(patient_id))
        if patient.exists():
            patient = patient.first()
        else:
            return JsonResponse({"status":"FAIL", "message":"patient does not exist"})
        try:
            if "age" in data:
                patient.age = data["age"]
            if "name" in data:
                patient.name = data["name"]
            if "lastname" in data:
                patient.lastname = data["lastname"]
            patient.save()
        except:
            return JsonResponse({"status":"FAIL", "message":"missing field"})
        return JsonResponse({"status":"OK", "message":""})