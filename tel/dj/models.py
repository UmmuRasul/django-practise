from django.db import models
from django.utils import timezone

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    date_adm = models.DateTimeField(auto_now_add=True)
    id_no = models.IntegerField()
    img = models.ImageField(upload_to='pics')