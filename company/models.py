from django.db import models

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Kompaniya haqida"

class Contact(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Kontaktlar"

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='employees/', blank=True, null=True)

    def __str__(self):
        return self.full_name
