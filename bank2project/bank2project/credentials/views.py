from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logouts


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('formpage')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')


            else:
                user = User.objects.create_user(username=username, password=password)


            user.save();
            return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')


    return render(request, "register.html")

def formpage(request):
    return render(request,"formpage.html")

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('index')
