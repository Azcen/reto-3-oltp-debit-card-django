from django.db import models


# Create your models here.
  
class User(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
  
class Account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  balance = models.DecimalField(decimal_places=2, max_digits=10)
  
  
class Card(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  balance = models.DecimalField(decimal_places=2, max_digits=10)
  