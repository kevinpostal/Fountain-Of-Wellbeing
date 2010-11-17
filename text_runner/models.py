from django.db import models

# Create your models here.

class Text_Log(models.Model):
    patient = models.ForeignKey('Patient')
    number_texted = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)

class Patient(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_msg = models.DateField(auto_now=True)
    msg_amount = models.PositiveIntegerField(blank=True,null=True)
    phone_number = models.CharField(max_length=50)
    def __str__(self):
        return "%s" % (self.name)

