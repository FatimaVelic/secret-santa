from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Participants (models.Model):
    giver = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True, related_name = "giver")
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True, related_name = "receiver")

    def __str__(self):
        return self.receiver.username