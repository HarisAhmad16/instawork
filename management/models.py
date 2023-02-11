from django.db import models

# Create your models here.
class TeamMember(models.Model):
    ROLE_CHOICES = (
        (1, 'Regular'),
        (2, 'Admin'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    role = models.IntegerField(choices=ROLE_CHOICES)