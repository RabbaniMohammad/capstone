from django.db import models
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    email = models.CharField(max_length=100, null = True, blank=True)
    password = models.CharField(max_length=10, null = True, blank = True)

    def __str__(self):
        return self.name