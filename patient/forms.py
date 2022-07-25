from pyexpat import model
from rest_framework import serializers
# from dataclasses import field
# from django.forms import ModelForm 
from . models import Patient

class PatientForm(serializers.ModelSerializer): 
    class Meta: 
        model = Patient 
        fields = "__all__"