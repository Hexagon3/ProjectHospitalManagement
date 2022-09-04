from django.db import models

# Create your models here.


class Nurse (models.Model):
    def __init__(self: _Self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = models.CharField(max_length=20)
        self.cost = 0
