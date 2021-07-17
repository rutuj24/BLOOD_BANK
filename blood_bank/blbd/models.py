from django.db import models

# Create your models here.
class donor(models.Model):
    donor_id = models.BigAutoField
    donor_name  = models.CharField(max_length=50)
    donor_age = models.IntegerField(default=0)
    donor_email = models.EmailField(max_length=50,default="")
    donor_gender = models.CharField(max_length=10)
    donors_blood_group = models.CharField(max_length=5)
    donor_Volume = models.DecimalField(max_digits=5,decimal_places=2)
    donor_date = models.DateField()
    def __str__(self):
        return self.donor_name

class receiver(models.Model):
    receivers_id = models.BigAutoField
    receivers_name  = models.CharField(max_length=50)
    receivers_age  = models.IntegerField(default=0)
    receivers_email = models.EmailField(max_length=50,default="")
    receivers_gender = models.CharField(max_length=10)
    receivers_blood_group = models.CharField(max_length=5)
    receivers_Volume = models.DecimalField(max_digits=5,decimal_places=2)
    receivers_date = models.DateField()
    def __str__(self):
        return self.receivers_name

class stocks(models.Model):
    A_positive = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    A_negative = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    B_positive = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    B_negative = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    O_positive = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    O_negative = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    AB_positive = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    AB_negative = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
