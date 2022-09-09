from django.urls import path
from .views import home, signup, login, patient_registration
urlpatterns = [
    path('', home),    # Domainname.com/
    path('user/signup', signup),
    # domain_name.com/user/signup
    path('user/login', login),
    # domain_name.com/user/login

    path('patient/registration', patient_registration),

]
