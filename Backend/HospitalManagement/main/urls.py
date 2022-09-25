from django.urls import path
from .views import home, signup, patient_registration, nurse_profile, logout_session, show_schedule, nurse_profile_update
urlpatterns = [
    path('', home),    # Domainname.com/
    path('user/signup', signup),
    # domain_name.com/user/signup
    path('user/nurse/profile/', nurse_profile),
    path('user/logout', logout_session),
    # domain_name.com/user/login

    path('patient/registration', patient_registration),
    path("user/nurse/schedule", show_schedule),
    path("user/nurse/setprofile", nurse_profile_update)

]
