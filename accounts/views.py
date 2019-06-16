from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        #uporabnik se želi logirat
        #sta gesli enaki?
        if request.POST['password1']==request.POST['password2']:
            try:#probaj ali uporabnik že obstaja? če ja vrni napako
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username already taken'})
                #če ne ustvari novega uporabnika
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'Passwords dont match'})
    else:
        #uporabnik želi vstop do informacij
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method=='POST':#preveri ali gre za post request
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])#ali gre za pravilne podatke(username password)
        if user is not None:
            auth.login(request,user)#če je vse prav ga vpiši
            return redirect('home')
        else:#če podatki niso pravi vrni napako
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method=='POST':#preveri ali gre za post request
        auth.logout(request)
        return redirect('home')
