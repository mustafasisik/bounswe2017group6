import unittest
import os
import subprocess
from django.test import TestCase
from .models import *
from django.test.client import RequestFactory
from .views import department_single, department
from .models import Department
from .views import patient_single, patient
from .models import Patient
from .views import rendezvous_single, rendezvous
from .models import Rendezvous
from .models import Doctor
from .views import doctor_single, doctor
from django.http import JsonResponse
import json

class RendezvousTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		d=Doctor.objects.create(name = "Erdal",lastname= "bakkal",age=44)
		p=Patient.objects.create(name = "Scobby",lastname= "Dobby",age=12)
		Rendezvous.objects.create(doctor=d,patient=p)
		
	
	def test_post_method(self):
		request = self.factory.post('/hospital/rendezvous/',json.dumps({"patient_id":"1","doctor_id":"1"}), content_type = 'application/json')
		response = rendezvous(request)
		self.assertEqual(response.status_code, 200)
		request = self.factory.get('/hospital/rendezvous/')
		response = rendezvous_single(request, 1)
		self.assertEqual(response.status_code, 200)
		rendez = Rendezvous.objects.filter(id = int(2)).first()
		self.assertEqual("Erdal bakkal", rendez.doctor.name+" "+rendez.doctor.lastname)
		self.assertEqual("Scobby Dobby", rendez.patient.name+" "+rendez.patient.lastname)

	def test_get_method(self):
		request = self.factory.get('/hospital/rendezvous/')
		response = rendezvous_single(request, 1)
		self.assertEqual(response.status_code, 200)
		rendezvous = Rendezvous.objects.filter(id = int(1)).first()
		self.assertEqual("Erdal bakkal", rendezvous.doctor.name+" "+rendezvous.doctor.lastname)
		self.assertEqual("Scobby Dobby", rendezvous.patient.name+" "+rendezvous.patient.lastname)

	def test_delete_method(self):
		request = self.factory.delete('/hospital/rendezvous/',json.dumps({"d.name": "Erdal"}), content_type = 'application/json')
		response = rendezvous_single(request, 1)
		self.assertEqual(response.status_code, 200)
		rendezvous = Rendezvous.objects.filter(id = int(1)).first()
		self.assertEqual(response.content, JsonResponse({"status": "OK", "message": ""}).content)
		
	def tearDown(self):
		Department.objects.all().delete()



class DoctorSingleTestCase(TestCase):
    def setUp(self):
        Doctor.objects.create(name="Deniz", lastname="Yilmaz", age="38")
        Doctor.objects.create(name="Firat", lastname="Tekin", age="29")
        Doctor.objects.create(name="Selin", lastname="Kir", age="41")

    def test_doctor_single_get(self):
        resp = self.client.get("/hospital/doctor/1/")
        expected = b'{"name": "Deniz", "lastname": "Yilmaz", "age": 38}'
        self.assertEqual(expected, resp.content)

        resp = self.client.get("/hospital/doctor/2/")
        expected = b'{"name": "Firat", "lastname": "Tekin", "age": 29}'
        self.assertEqual(expected, resp.content)

        resp = self.client.get("/hospital/doctor/3/")
        expected = b'{"name": "Selin", "lastname": "Kir", "age": 41}'
        self.assertEqual(expected, resp.content)

    def test_doctor_single_put(self):
        data = {"name": "Asya", "lastname": "Tarik", "age": "33"}
        resp = self.client.put("/hospital/doctor/1/",
                               json.dumps(data),
                               content_type="application/json")
        expected = b'{"status": "OK", "message": ""}'
        self.assertEqual(expected, resp.content)

        data = {"name": "Asya", "lastname": "Tarik"}
        resp = self.client.put("/hospital/doctor/2/",
                               json.dumps(data),
                               content_type="application/json")
        expected = b'{"status": "OK", "message": ""}'
        self.assertEqual(expected, resp.content)

        data = {"name": "Asya", "lastname": "Tarik", "age": "33"}
        resp = self.client.put("/hospital/doctor/6/",
                               json.dumps(data),
                               content_type="application/json")
        expected = b'{"status": "FAIL", "message": "doctor does not exist"}'
        self.assertEqual(expected, resp.content)

    def tearDown(self):
        Doctor.objects.all().delete()


class DepartmentTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		Department.objects.create(name = "yuz kafa bas")
		Department.objects.create(name = "deliler kismi")
	
	def test_get_method(self):
		request = self.factory.get('/hospital/department/')
		response = department_single(request, 1)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, JsonResponse({"name": "yuz kafa bas"}).content)
	
	def test_put_method(self):
		request = self.factory.put('/hospital/department/', json.dumps({"name": "tirnak burun sac"}), content_type = 'application/json')
		response = department_single(request, 1)
		self.assertEqual(response.status_code, 200)
		department = Department.objects.filter(id = int(1)).first()
		self.assertEqual("tirnak burun sac", department.name)

	def tearDown(self):
		Department.objects.all().delete()

class PatientTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		Patient.objects.create(name = "Kazim", lastname= "Kazim", age=34)
		Patient.objects.create(name = "Tahm", lastname= "Kench", age=91)
	
	def test_get_method(self):
		request = self.factory.get('/hospital/patient/')
		response = patient_single(request, 1)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, JsonResponse({"name": "Kazim", "lastname":"Kazim", "age": 34}).content)
	
	def test_put_method(self):
		request = self.factory.put('/hospital/patient/', json.dumps({"name": "Salih"}), content_type = 'application/json')
		response = patient_single(request, 1)
		self.assertEqual(response.status_code, 200)
		patient = Patient.objects.filter(id = int(1)).first()
		self.assertEqual("Salih", patient.name)
	def test_post_method(self):
		request = self.factory.post('/hospital/patient', json.dumps({"name": "Muhittin", "lastname" : "Yilmaz" , "age" : 50}), content_type = 'application/json')
		response = patient(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, JsonResponse({"status": "OK", "message": ""}).content)
	def test_delete_method(self):
		request = self.factory.delete('/hospital/patient',json.dumps({"name": "Kazim"}), content_type = 'application/json')
		response = patient_single(request, 1)
		self.assertEqual(response.status_code, 200)
		patient = Patient.objects.filter(id = int(1)).first()
		self.assertEqual(response.content, JsonResponse({"status": "OK", "message": ""}).content)
	def tearDown(self):
		Patient.objects.all().delete()
class DoctorPostCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
	def test_post_method(self):
		request = self.factory.post('/hospital/doctor/',json.dumps({"name":"ahmet","lastname":"kısa","age":32}), content_type = 'application/json')
		response = doctor(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, JsonResponse({"status": "OK", "message": ""}).content)
	def tearDown(self):
		Department.objects.all().delete()

