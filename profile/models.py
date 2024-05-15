from django.db import models
from  django.conf import settings

from PIL import Image


# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(upload_to = 'covers/'  , default='covers/Annotation_2022-08-10_011419.png')
    bio = models.CharField(max_length=300)
    first_name = models.CharField(max_length = 200 , default='user.first_name')
    last_name = models.CharField(max_length = 200 , default='user.last_name')
    phone_number = models.IntegerField()
    national_code = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)



class InformationCart(models.Model):
    number_cart = models.CharField(max_length=30)
    number_account_cart = models.CharField(max_length=30)
    number_shabaa_cart = models.CharField(max_length=50)
    cvv2 = models.PositiveSmallIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)





