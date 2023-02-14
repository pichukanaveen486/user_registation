from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail


def home(request):
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