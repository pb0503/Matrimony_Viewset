from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Family(models.Model):
    family_values=models.CharField(max_length=100)
    family_type=models.CharField(max_length=100)
    family_status=models.CharField(max_length=100)
    no_of_brothers=models.IntegerField()
    no_of_brothers_married=models.IntegerField()
    no_of_sisters=models.IntegerField()
    no_of_sisters_married=models.IntegerField()
    mothertounge=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    father_occupation=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    mother_occupation=models.CharField(max_length=100)
    family_wealth=models.IntegerField()
    about_family=models.CharField(max_length=100)
    
