
from django.shortcuts import render

# Create your views here.


def control_panel(req, catagory=None, form_type=None):
    print(form_type)
    return render(req, 'Admin_2.html')


def profile(req):
    return render(req, 'AdminsProfile.html')


def nurse_schedule(req):
    pass
