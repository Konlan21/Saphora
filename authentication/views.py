from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        return redirect('login')
    return render(request, 'authentication/login_user.html', {})