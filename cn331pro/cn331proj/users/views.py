from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/subject_list')
        else:
            messages.success(request,("There was an errror logging in, Try again"))
            return redirect('/users/login_user')
    else:
        return  render(request, 'login.html')
    
def get_username(request):
    username = request.POST["username"]
    return username
    

# def goSubject(request):
#     return redirect("subject_list.html")

# def userCheck(request):
#     users = User.objects.all()
#     user = User.objects.get(id=1)  # เปลี่ยน 1 เป็น ID ที่ต้องการ
#     user = User.objects.get(username='username_here')
