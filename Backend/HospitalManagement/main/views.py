from django.shortcuts import render
from django.http import HttpResponse
from .models import Nurse
# Create your views here.


def home(req):
    user = {'logedin': True}
    context = {'user': user}
    return render(req, "home.html", context=context)


def login(req):
    pass


def signup(req):
    if req.method == 'POST':
        firdt_name = req.POST.get("firstName")
        last_name = req.POST.get("lastName")
        email = req.POST.get("email")

        # passwd2 = req.POST.get('password2')

        passwd1 = req.POST.get('password1')
        for nurse in Nurse.objects.all():
            if nurse.email == email:
                return render(req, "Signup_Page.html")
        new_nurse = Nurse(
            name=firdt_name+' '+last_name,
            email=email,
        )
        new_nurse.set_password(passwd1)
        new_nurse.save()
        return HttpResponse("Registration Success")

    return render(req, "member_login.html")


def nurse_profile(req, nurse):
    return HttpResponse(
        '''
        <h1> Nurse Profile </h1>

        '''
    )


def doctor_profile(req, nurse):
    return HttpResponse(
        '''
        <h1> Doctor Profile </h1>

        '''
    )


def patient_registration(req):
    return render(req, "patient_registration.html")
