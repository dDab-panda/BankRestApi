from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.BigIntegerField(null=True)
    branch = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=30, null=True)
    bank_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ifsc