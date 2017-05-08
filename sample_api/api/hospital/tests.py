import unittest
import os
import subprocess
from django.test import TestCase
from django.test.client import RequestFactory
from .views import department_single, department
from .models import Department
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
