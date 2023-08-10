from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    subject = models.CharField(max_length=240)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)