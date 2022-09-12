
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Nurse (models.Model):
    # def __init__(self, *args, **kwargs) -> None:
    # #     super().__init__(*args, **kwargs)
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(null=True)
    bio = models.TextField(null=True)
    email = models.EmailField()
    address = models.TextField(null=True)
    license = models.CharField(max_length=12, null=True)
    contact_no = models.CharField(max_length=10, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cost = 0
    allocated_word = None
    shift = None

    def __str__(self) -> str:
        return "nurse : "+self.name


class Patient(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=30, null=True)
    adhar_no = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=10, null=True)
    word_id = models.IntegerField()
    room_no = models.IntegerField()

    def __str__(self):
        return self.name
    # class Doctor(models.Model):
    #     name = models.CharField(max_length=20, default="Nurse")
    #     profile_pic = models.ImageField(null=True)
    #     # bio = models.TextField(null=True)
    #     email = models.EmailField(null=True)

    #     def __str__(self):
    #         return "Dr."+self.name


class Word(models.Model):
    MAX_BED = models.IntegerField()
    active_bed = models.IntegerField()

    def __srt__(self):
        return self.id
