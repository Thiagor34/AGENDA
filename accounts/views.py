from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = auth.authenticate(username=username, password=password)
        
        if check_user == None:
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')
        
    else:
        return render(request, 'pages/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('login')