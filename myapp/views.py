from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,JsonResponse
from .models import Doc

# Create your views here.

class Home(TemplateView):
    template_name = 'upload.html'

def file_upload(request):
    if request.method=="POST":
        my_file = request.FILES.get('file')
        Doc.objects.create(upload=my_file)
        return HttpResponse('')

    return  JsonResponse({'post':'false'})