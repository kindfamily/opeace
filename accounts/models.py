from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=30, unique=True)
    remained_time = models.IntegerField('잔여시간(분)')
    used_status = models.CharField('사용중여부', max_length=1, default='N')
    
    def __str__(self):
        return self.nickname