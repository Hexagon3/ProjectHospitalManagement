from django.db import models

# Create your models here.


class Nurse (models.Model):
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    name = models.CharField(max_length=20)
    profile_pic = models.ImageField(null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    license = models.CharField(max_length=12, null=True)
    contact_no = models.CharField(max_length=10, null=True)
    cost = 0
    allocated_word = None
    shift = None

    def __str__(self) -> str:
        # return super().__str__()
        return "Nurse"+str(self.id)
