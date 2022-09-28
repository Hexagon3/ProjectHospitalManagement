
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Nurse, User, Patient
from django.contrib.auth import authenticate, login, logout
from datetime import date
from .form import ImageUpload
from .scheduling import generate_bed_no
# Create your views here.


def home(req: HttpRequest):
    # logout(User.objects.get(username='admin'))

    user = {'logedin': req.user.is_authenticated}
    context = {'user': user}
    return render(req, "home.html", context=context)


def signup(req):
    if req.method == 'POST':
        try:
            username = req.POST.get("username")
            email = req.POST.get("email")
            passwd2 = req.POST.get('psswd2')
            passwd1 = req.POST.get('psswd1')
            print(passwd1)
            if passwd1 == None:
                raise "f"
            print(passwd1)
            if (passwd1 == passwd2):
                user = User.objects.create_user(
                    username=username, email=email, password=passwd2)
                n1 = Nurse(username=username, email=email, name=username,
                           user=user)
                n1.save()
                login(req, n1.user)
                print("login Success")

                user = {'logedin': req.user.is_authenticated}
                context = {'user': user}
                return redirect("/")
            else:
                context = {"message": "Login faild"}
                return render(req, "member_login.html", context)
        except:
            email = req.POST.get("email")
            passwd = req.POST.get('password')
            try:
                nurse = Nurse.objects.get(email=email)
            except:
                return render(req, "member_login.html")
            user = nurse.user  # authenticate(request)

            print(user)
            if user.check_password(passwd):
                print(user)
                login(req, user)
                return redirect("/")
            else:
                return render(req, "member_login.html")

    return render(req, "member_login.html")


def logout_session(req: HttpRequest):
    logout(req)
    return redirect('/')


def nurse_profile(req):
    print(req.user.nurse)
    active_nurse = Nurse.objects.get(username=req.user.username)
    context = {"nurse": active_nurse}
    return render(req, 'Bio.html', context=context)
    # return HttpResponse(f'<h1> Nurse Profile </h1>')


def show_schedule(req):

    nurse_email = req.user.email
    nurse = Nurse.objects.get(email=nurse_email)
    # if nurse.last_update_date == date.today():
    schedule_info = {
        'shift': nurse.shift,
        'word': nurse.allocated_word
    }

    return render(req, "pop_up_new.html",
                  context={'schedule': schedule_info})


def nurse_profile_update(req):
    if req.method == "POST":
        # form = ImageUpload(req.POST, req.FILES)

        first_name = req.POST.get("first_name")
        middle_name = req.POST.get("middle_name")
        last_name = req.POST.get("last_name")

        name = first_name+" "+middle_name+" "+last_name
        gender = req.POST.get('gender')
        age = req.POST.get('age')
        # profile_pic = req.FILES['image']

        bio = req.POST.get('bio')
        address = req.POST.get('age')
        # license_no  =  req.POST.get('license')
        contact_no = req.POST.get('phn_no')
        experience = req.POST.get('experience')
        department = req.POST.get('department')
        # email = req.POST.get("email")
        # password = req.POST.get("password1")

        nurse = req.user.nurse

        # nurse.name = name
        # nurse.profile_pic = profile_pic
        nurse.bio = bio
        nurse.gender = gender
        nurse.address = address
        # nurse.license = license_no
        nurse.contact_no = contact_no
        nurse.experience = experience
        nurse.department = department

        nurse.save()
        # if form.is_valid():
        #     form.save()
        return redirect('/user/nurse/profile')

    form = ImageUpload()
    if (req.user.is_authenticated):
        return render(req, "nurse_form.html",  {'form': form})


def doctor_profile(req, nurse):
    return HttpResponse(
        '''
        <h1> Nurse Profile </h1>

        '''
    )


def patient_registration(req):
    if req.method == "POST":
        name = req.POST.get("name")
        phone = req.POST.get("phone")
        email = req.POST.get("email")
        adhar = req.POST.get("adhar")
        address = req.POST.get("address")
        female = req.POST.get("female")
        male = req.POST.get("male")
        other = req.POST.get("other")
        word_id = generate_bed_no()
        if male == True:
            gender = 'male'
        elif female == True:
            gender = 'female'
        else:
            gender = 'other'

        patient = Patient(
            name=name,
            phone=phone,
            email=email,
            adhar_no=adhar,
            address=address,
            gender=gender,
            word_id=word_id

        )
        patient.save()
        # return redirect("/")
    return render(req, "patient_registration.html")
