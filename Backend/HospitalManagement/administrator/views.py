
from django.shortcuts import render

# Create your views here.
def control_panel(req, catagory=None, form_type=None) :
    print(form_type)
    return render(req, 'control_panel.html')

def profile(req) :
    pass

def nurse_schedule(req) :
    pass
