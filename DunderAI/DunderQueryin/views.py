from django.shortcuts import render
from django.http import HttpResponse

def dunder_ai(request):
    return render(request, 'DunderQueryin/dunder_ai.html', {})

# Create your views here.