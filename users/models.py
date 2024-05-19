from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    profile_picture = models.CharField(max_length=255, blank=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    activation_link = models.CharField(max_length=255, blank=True)
    activation_status = models.BooleanField(default=False)
    admin = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinates')

    def __str__(self):
        return self.email
