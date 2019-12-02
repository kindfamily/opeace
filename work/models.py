from django.db import models
from accounts.models import Profile

# Create your models here.
class WorkHistory(models.Model):
    profile = models.ForeignKey(Profile, null=True, related_name="work_histories", on_delete=models.CASCADE)
    worked_at = models.DateTimeField(auto_now_add=True)
    work_type = models.CharField('타입', max_length=1, default='N')