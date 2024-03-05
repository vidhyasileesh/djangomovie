from django.db import models

# Create your models here.

class Cards(models.Model): #DB table definition in Django
    title= models.CharField(max_length=20)
    desc=models.CharField(max_length=50)
    year=models.IntegerField(default=0)
    image=models.ImageField(upload_to="card/image",null=True,blank=True)

    def __str__(self):
        return self.title


