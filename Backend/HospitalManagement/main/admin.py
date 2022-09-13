from django.contrib import admin

# Register your models here.
from .models import Nurse, Patient, Word
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Word)
