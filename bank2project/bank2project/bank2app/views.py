
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')



