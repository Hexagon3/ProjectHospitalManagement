from django.urls import path
from .views import home, signup
urlpatterns = [
    path('', home),
    path('user/signup', signup),

]
