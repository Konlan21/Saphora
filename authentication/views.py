from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.success(request, 'There was an error logging in, Please try again..')
        return redirect('customer-login')
    return render(request, 'authentication/login_user.html', {})



def logout_customer(request):
    logout(request)
    return redirect('store')


def register_customers(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register_customers.html', {'form': form})