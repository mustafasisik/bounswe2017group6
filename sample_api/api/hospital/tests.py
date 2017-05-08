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
from django.http import JsonResponse
import json

class Test1(TestCase):
	def test_rendezvous_get(self):
		result = subprocess.getoutput('http --json GET http://127.0.0.1:8000/hospital/rendezvous/1/')
		expected='{"Patient": "qwer qwerty", "Doctor Name": "Kazim Kazim", "Time": "2017-04-23 22:07:39.117858+00:00"}'
		self.assertEqual(expected,result)
	def test_rendezvous_post(self):
		result = subprocess.getoutput('http --json POST http://127.0.0.1:8000/hospital/rendezvous/ patient_id=3 doctor_id=1')
		expected='{"status": "OK", "message": "rendezvous added"}'
		self.assertEqual(expected,result)



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

	def tearDown(self):
		Patient.objects.all().delete()
