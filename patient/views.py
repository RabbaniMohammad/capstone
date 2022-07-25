from django.shortcuts import render
from . forms import PatientForm
from rest_framework.views import APIView 
from rest_framework.response import Response
from . models import Patient
import json
# Create your views here.

class Auth(APIView): 
    def post(self, request): 
        response = {}
        data = request.data 
        checking = data.get("token")
        if checking == "signup":
            email = data.get("email")
            obj = PatientForm(data = request.data)
            check = Patient.objects.filter(email = email)
            try:
                if len(check) >= 1:
                    response['message'] = "account exists"
                    return Response(response)
                if obj.is_valid():
                    response['message'] = 200 
                    obj.save()
                    return Response(response)
                return Response(response)
            except Exception as e:
                return Response(obj.errors)
        email = data.get("email")
        password = data.get("password")
        try:
            obj = Patient.objects.get(email = email)
            if obj.email == email and obj.password == password:
                response = {}
                response['message'] = 200 
                response['name'] = obj.name 
            
                return Response(response)
            return Response({"message":"invalid credentials"})
        except Exception as e:
            return Response({"message":"invalid credentials"}) 
        


Auth = Auth.as_view()