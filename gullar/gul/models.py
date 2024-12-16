from django.db import models

# Create your models here.
class Turlar(models.Model):
    name=models.CharField(max_length=100,verbose_name='tur nomi')
    def __str__(self):
        return self.name




class Gullar(models.Model):
    tur=models.ForeignKey(Turlar,on_delete=models.CASCADE,verbose_name='gul turi')
    name=models.CharField(max_length=100,verbose_name='gul nomi')
    color=models.CharField(max_length=13,verbose_name='gul rangi')
    about=models.TextField(null=True,blank=True)
    photo=models.ImageField(upload_to='media/photos/')
    def __str__(self):
        return self.name
