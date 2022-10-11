from django.urls import path
from .views import control_panel, profile, nurse_schedule_display
urlpatterns = [

    # path('control-panel/<catagory:str>/<form_type:str>',control_panel),
    path('control-panel/<str:catagory>/<str:form_type>/', control_panel),
    path('control-panel/<str:catagory>/', control_panel),
    path('control-panel/', control_panel),
    path('profile', profile),
    path('nurse-schedule', nurse_schedule_display),

]
