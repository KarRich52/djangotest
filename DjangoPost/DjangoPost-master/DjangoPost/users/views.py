from django.shortcuts import render, redirect
from .forms import LoginForms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def sign_in(request):

   if request.method == 'GET':

       if request.user.is_authenticated:

           return redirect('home')

       form = LoginForms()

       return render(request,'users/login.html', {'form': form})

   elif request.method == 'POST':

       form = LoginForms(request.POST)

       if form.is_valid():

           username = form.cleaned_data['username']

           password=form.cleaned_data['password']

           user = authenticate(request,username=username,password=password)

           if user:

               login(request, user)

               messages.success(request,f'Hi {username.title()}, welcome back!')

               return redirect('home')


def sign_out(request):
    logout(request)
    messages.success(request, f'Вы вышли из аккаунта.')
    return redirect('login')