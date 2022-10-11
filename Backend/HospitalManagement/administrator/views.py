
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
        if form_type == -1 and catagory == "nurse":
            username = req.POST.get("username")
            email = req.POST.get("email")
            try:
                User.objects.get(email=email)
                context = {'catagory': catagory,
                           'form_type': form_type,
                           "message": "This Email is exist"}
                return render(req, 'Admin_2.html', context=context)
            except:
                pass
            try:
                t = User.objects.get(username=username)
                context = {'catagory': catagory,
                           'form_type': form_type,
                           "message": "This username is exist"}
                return render(req, 'Admin_2.html', context=context)
            except:
                pass
            name = req.POST.get("name")
            age = req.POST.get("age")
            contact_no = req.POST.get("phn_no")
            address = req.POST.get("add")
            department = req.POST.get("types")
            experience = req.POST.get("experience")
            password = req.POST.get("password")
            user = User.objects.create_user(
                username=username, email=email, password=password)
            n1 = Nurse(username=username, email=email, name=username,
                       user=user)
            try:
                n1.name = name
            except:
                n1.name = n1.username
            try:
                n1.age = age
            except:
                n1.age = -1
            try:
                n1.contact_no = contact_no
            except:
                n1.contact_no = "None"
            try:
                n1.department = department
            except:
                n1.department = "None"
            try:
                n1.experience = experience
            except:
                n1.experience = 0
                pass
            n1.save()
        elif catagory == "nurse":
            user = User.objects.get(id=form_type)
            nurse = user.nurse
            nurse.name = req.POST.get("name")
            nurse.age = req.POST.get("age")
            nurse.contact_no = req.POST.get("phn_no")
            nurse.address = req.POST.get("add")
            nurse.department = req.POST.get("types")
            nurse.experience = req.POST.get("experience")
            nurse.password = req.POST.get("password")
            nurse.save()
        elif form_type == -1 and catagory == "word":
            MAX_BED = req.POST.get("max_bed")
            active_bed = req.POST.get("active_bed")
            word = Word()
            word.MAX_BED = MAX_BED
            word.active_bed = active_bed
            word.save()

        elif catagory == "word":
            MAX_BED = req.POST.get("max_bed")
            active_bed = req.POST.get("active_bed")
            word = Word.objects.get(id=form_type)
            word.MAX_BED = MAX_BED
            word.active_bed = active_bed

        return redirect("/administrator/control-panel")

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
    return render(req, 'nurse_schedule.html')
