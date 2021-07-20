from django.db import models
import datetime


# Create your models here.
burger_choices = (('BK fried chicken', 'BK fried chicken'), ('Friends combo', 'Friends combo'),
                  ('Family combo', 'Family combo'),
('Chiken Wings', 'Chiken Wings'))

gender_choices=(('male', 'male'),('female', 'female'))

class Seller(models.Model):
    uname=models.CharField(max_length=50)
    mobno=models.CharField(max_length=10)
    email=models.EmailField()
    burg_type=models.CharField(max_length=50, choices=burger_choices)
    burg_image=models.ImageField(upload_to='images/')
    gender=models.CharField(max_length=30, choices=gender_choices)
    order_date=models.DateField(default=datetime.datetime.today)

