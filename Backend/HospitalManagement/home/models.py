from django.db import models

# Create your models here.


class Nurse (models.Model):
    def __init__(self: _Self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = models.CharField(max_length=20)
        self.profile_pic = models.ImageField()
        self.bio = models.TextField()
        self.email = models.EmailField()
        self.address = models.TextField()
        self.license = models.CharField(max_length=12)
        self.contact_no = models.CharField(max_length=10)
        self.cost = 0
        self.allocated_word = None
        self.shift = None
