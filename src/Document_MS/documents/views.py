from django.shortcuts import render
from . models import ProjectName, Documents
from django.http import HttpResponse

def welcoming(request):
    return render(request, 'documents/welcome.html')
