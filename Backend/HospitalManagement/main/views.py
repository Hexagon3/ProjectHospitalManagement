from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    return HttpResponse(
        """
        <h1>Project : Hospital Management System </h1>
        <h2> Sub Project : Nurse Scheduling in bed </h2>
        <p> Design the ui of home page and then it will looks better </p>
        """
    )


def signup(req):
    if req.method == 'POST':
        return HttpResponse("h1")

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
