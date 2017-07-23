from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_info(models.Model):
    user_id = models.IntegerField();
    user_name = models.CharField(max_length = 100);
    user_interest = models.CharField(max_length= 100);
    
    def __str__(self):
        return self.user_name;
    
    