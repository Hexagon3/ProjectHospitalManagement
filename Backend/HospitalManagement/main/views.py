from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Nurse, User, Patient
from django.contrib.auth import authenticate, login, logout
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
            passwd2 = req.POST.get('passwd2')
            passwd1 = req.POST.get('passwd1')

            if (passwd1 == passwd2):
                n1 = Nurse(username=username, email=email, name=username)
                n1.user = User.objects.create_user(
                    username=username, email=email, password=passwd2)
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
            if user.check_password(passwd):
                login(req, user)
                return redirect("/")
            else:
                return render(req, "member_login.html")

    return render(req, "member_login.html")


def logout_session(req: HttpRequest):
    logout(req)
    return redirect('/')


def nurse_profile(req):

    active_nurse = Nurse.objects.get(username=req.user.username)
    context = {"nurse": active_nurse}
    return render(req, 'Bio.html', context=context)
    # return HttpResponse(f'<h1> Nurse Profile </h1>')


def show_schedule(req):

    return render(req, "pop_up_new.html")


def nurse_set_info(req):
    # return render("  ")
    return HttpRequest("Nurse Details")


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
            gender=gender

        )
        patient.save()
        # return redirect("/")
    return render(req, "patient_registration.html")
