from django.db import models

# Create your models here.
class From2(models.Model):
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)
    father_name = models.CharField(max_length=25,blank=True)
    mother_name = models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=40,blank=True)
    address = models.CharField(max_length=55,blank=True)
    city= models.CharField(max_length=20,blank=True)
    number = models.CharField(max_length=10)
    number1 = models.CharField(max_length=12)
    
   
    #Aadhrnumber=models.IntegerField()
   
    def __str__(self):
        return self.first