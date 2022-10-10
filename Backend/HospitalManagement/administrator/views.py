
from tokenize import Special
from django.shortcuts import render, redirect
from main.models import Nurse, Word, User
# Create your views here.


def control_panel(req, catagory=None, form_type=None):
    try:
        form_type = int(form_type)
    except:
        form_type = None
        #
    if req.method == 'POST':
        if form_type == -1:
            username = req.POST.get("username")
            password = req.POST.get("password")
            email = req.POST.get("email")
            user = User.objects.create_user(
                username=username, email=email, password=password)
            n1 = Nurse(username=username, email=email, name=username,
                       user=user)
            n1.name = req.POST.get("name")
            n1.age = req.POST.get("age")
            n1.contact_no = req.POST.get("phn_no")
            n1.address = req.POST.get("add")
            n1.department = req.POST.get("types")
            n1.experience = req.POST.get("experience")
            n1.save()
        return redirect("/administrator/controlpanel")
    context = {
        'catagory': catagory,
        'form_type': form_type,
        'nurses': Nurse.objects.all(),
        'words': Word.objects.all(),
    }
    if catagory == 'nurse':
        if form_type is not None and form_type > 0:
            context['nurse_selected'] = User.objects.get(id=form_type).nurse
    elif catagory == 'word':
        if form_type is not None and form_type > 0:
            context['word_selected'] = Word.objects.get(id=form_type)

    return render(req, 'Admin_2.html', context=context)


def profile(req):
    return render(req, 'AdminsProfile.html')


def nurse_schedule(req):
    pass
