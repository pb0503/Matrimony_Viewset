from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class ContactUS(models.Model):
    mobile_number=models.IntegerField()
    Alternate_Mob_No=models.IntegerField()
    Convinient_time_to_call=models.TimeField()
    email=models.EmailField()
    Permanent_Address=models.TextField()
    Working_address=models.TextField()