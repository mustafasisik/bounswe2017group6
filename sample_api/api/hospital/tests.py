import unittest
import os
import subprocess
from django.test import TestCase
from .models import *
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
