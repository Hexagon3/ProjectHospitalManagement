
from django.db import models

# Create your models here.


class Nurse (models.Model):
    # def __init__(self, *args, **kwargs) -> None:
    # #     super().__init__(*args, **kwargs)
    name = models.CharField(max_length=20, default="Nurse")
    profile_pic = models.ImageField(null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    __password: str
    address = models.TextField(null=True)
    license = models.CharField(max_length=12, null=True)
    contact_no = models.CharField(max_length=10, null=True)
    __logged_in = False
    cost = 0
    allocated_word = None
    shift = None

    def __str__(self) -> str:
        return "nurse : "+self.name

    def set_password(self, passwd: str):
        self.__password = passwd

    def verify_password(self, passwd: str):
        return (self.__password == passwd)

    def is_logged_in(self):
        return self.__logged_in

    def login(self):
        self.__logged_in = True


class Doctor(models.Model):
    name = models.CharField(max_length=20, default="Nurse")
    profile_pic = models.ImageField(null=True)
    # bio = models.TextField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return "Dr."+self.name
