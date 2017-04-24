from django.db import models

# Create your models here.

# doctor create         (post)
# doctor get            (get) by_id / all
# doctor update         (update) by_id
# doctor delete         (delete) by_id
class Doctor(models.Model): # 5
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.lastname + "(" + str(self.age) + ")"

# patient create        (post)
# patient get           (get) by_id / all
# patient update        (update) by_id
# patient delete        (delete) by_id
class Patient(models.Model): # 10
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.lastname + "(" + str(self.age) + ")"

# rendezvous create     (post)
# rendezvous get        (get) by_id / all
# rendezvous update     (update) by_id
# rendezvous delete     (delete) by_id
# rendezvous dismiss
class Rendezvous(models.Model): # 16
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")

    def __str__(self):
        return str(self.date) + " - " + str(self.doctor) + " - " + str(self.patient)

# department create     (post)
# department get        (get) by_id / all
# department update     (update) by_id
# department delete     (delete) by_id
# department assign to doctor
class Department(models.Model): # 22
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    doctors = models.ManyToManyField(Doctor,related_name="%(app_label)s_%(class)s_assigned")

    def __str__(self):
        return self.name
