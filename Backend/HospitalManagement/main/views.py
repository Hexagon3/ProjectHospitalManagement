from django.shortcuts import render
from django.http import HttpResponse
from .models import Nurse, User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(req):
    user = {'logedin': True}
    context = {'user': user}
    return render(req, "home.html", context=context)


def signup(req):
    if req.method == 'POST':
        try:
            username = req.POST.get("username")
            email = req.POST.get("email")
            passwd2 = req.POST.get('passwd2')
            passwd1 = req.POST.get('passwd1')
            if (passwd1 == passwd2):
                n1 = Nurse(username=username, email=email, name=username)
                n1.user = User.objects.create_user(
                    username=username, email=email, password=passwd2)
        except:
            email = req.POST.get("email")
            passwd = req.POST.get('password')
            nurse = Nurse.objects.get(email=email)
            user = authenticate(nurse.username, passwd)
            login(req, user)
        #     render(req, "Signup_Page.html")
        # new_nurse = Nurse(
        #     name=firdt_name+' '+last_name,
        #     email=email,
        # )
        # new_nurse.set_password(passwd1)
        # new_nurse.save()
        return HttpResponse("Registration Success")

    return render(req, "member_login.html")


def nurse_profile(req):
    return HttpResponse(

        f'<h1> Nurse Profile </h1>'


    )


def doctor_profile(req, nurse):
    return HttpResponse(
        '''
        <h1> Nurse Profile </h1>

        '''
    )


def patient_registration(req):
    return render(req, "patient_registration.html")
