from django.shortcuts import render
from django.http import JsonResponse

def htmx_home(request):
    return render(request, 'htmx/htmx.html')