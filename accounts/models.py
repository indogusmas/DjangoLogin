from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
