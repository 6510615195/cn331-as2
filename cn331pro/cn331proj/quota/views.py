from django.shortcuts import render
from django.http import HttpResponse
from quota.models import Subject

# Create your views here.

def index(request):
    return render(request,'index.html')

def subject_list(request):
    all_subject = Subject.objects.all()
    return render(request,'subject_list.html',{"all_subject":all_subject})

def my_quota(request):
    return render(request,'my_quota.html')

