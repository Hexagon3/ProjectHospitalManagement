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
