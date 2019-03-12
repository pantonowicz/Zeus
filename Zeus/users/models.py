from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

PROFILE_ROLE_CHOICES = [
    (0, "Sales Team"),
    (1, "Evalutaion Team"),
    (2, "Calculation Team"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=PROFILE_ROLE_CHOICES, default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.role} Member - {self.user.first_name}, {self.user.last_name} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
