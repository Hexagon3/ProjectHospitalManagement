from django.urls import path
from .views import home, signup, patient_registration, nurse_profile
urlpatterns = [
    path('', home),    # Domainname.com/
    path('user/signup', signup),
    # domain_name.com/user/signup
    path('user/nurse/profile/<str:username>', nurse_profile),
    # domain_name.com/user/login

    path('patient/registration', patient_registration),

]
