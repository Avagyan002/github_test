from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegistrationForm
from .models import SiteUser
import json


def register(request):
    try:
        data = json.load(request.body)
        form = RegistrationForm(data)
        if form.is_valid():
            user = form.save()
            response_data = {
                'success': True,
                'massage': 'Registration successful',
                'user_id': user.id,
            }
            return JsonResponse(response_data)
        else:
            errors = form.errors
            response_data = {
                'success': False,
                'massage': 'Registration failed',
                'errors': errors
            }
            return JsonResponse(response_data, status=400)
    except json.JSONDecodeError:
        response_data = {
            'success': False,
            'massage': 'Invalid JSON data',
        }
        return JsonResponse(response_data, status=400)
    
