from django.shortcuts import render
from django.http import HttpResponse
from .models import Nurse
# Create your views here.


def home(req):
    return HttpResponse(
        """
        <h1>Project : Hospital Management System </h1>
        <h2> Sub Project : Nurse Scheduling in bed </h2>
        <p> Design the ui of home page and then it will looks better </p>
        """
    )


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

    return render(req, "Signup_Page.html")


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
