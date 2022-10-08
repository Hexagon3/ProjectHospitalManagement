
from django.shortcuts import render
from main.models import Nurse, Word, User
# Create your views here.


def control_panel(req, catagory=None, form_type=None):
    try:
        form_type = int(form_type)
    except:
        form_type = None
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
