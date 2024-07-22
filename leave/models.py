from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Leave(models.Model):
    STATUS =[
        ('Approve','Approve'),
        ('Decline','Decline'),
         ('Pending','Pending'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comment = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,choices=STATUS,default='Pending',null=True,blank=True)
    admin_comment = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)