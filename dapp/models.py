from django.db import models

# Create your models here.

class Dapp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField(null=True)
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
