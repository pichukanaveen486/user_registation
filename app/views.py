from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required








def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}

        return render(request,'home.html',d)
    return render(request,'home.html') 
def register(request):
    uf=UserForm()   
    pf=ProfielForm()
    d={'uf':uf,'pf':pf}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfielForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            UFO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            UFO.set_password(password)
            UFO.save()




            PFO=PFD.save(commit=False)
            PFO.profile_user=UFO
            PFO.save()



            send_mail('registation form ', 'Thanks for registration , your registration is succusseful!', 'naveenpichuka143@gmail.com', [UFO.email],fail_silently=True)

            return HttpResponse('Registation is successfull')

        


    return render(request,'register.html',d)      



def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))

        else:
            return HttpResponse('the user is not authenticated')    
    return render(request,'user_login.html')




@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))





  

