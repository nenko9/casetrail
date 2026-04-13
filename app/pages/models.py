from django.db import models

# Create your models here.
class Requirements(models.Model):
    r_id = models.CharField(max_length=200, default=None)
    body = models.CharField(max_length=200, default=None, blank=False)
