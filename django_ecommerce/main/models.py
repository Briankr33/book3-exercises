from django.db import models
from payments.models import User

# Create your models here.
class MarketingItem(models.Model):
    img = models.CharField(max_length=255)
    heading = models.CharField(max_length=300)
    caption = models.TextField()
    button_link = models.URLField(null=True, default="register")
    button_title = models.CharField(max_length=20,default="View details")

class StatusReport(models.Model):
    user = models.ForeignKey(User)
    when = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)







