from django.contrib.auth.models import User
from django.db import models

PROFILE_ROLE_CHOICES = [
    (0, "Sales representative"),
    (1, "Evalutaion Team"),
    (2, "Calculation Team"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}, {self.user.last_name} Profile'
