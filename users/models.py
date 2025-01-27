from django.db import models
from django.contrib.auth.models import User



class UserProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=13)
    experience = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    wares = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if 1 >= self.experience < 3:
            self.wares = 1000
        elif 3 >= self.experience < 5:
            self.wares = 2000
        elif 5 >= self.experience < 7:
            self.wares = 5000
        else:
            self.grade = 'Experience must be greater than 1'

        super().save(*args, **kwargs)
