from django.db import models

# Create your models here.
class Shelter(models.Model):
    image=models.ImageField(upload_to='images/shelter', blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name
    
class Animal(models.Model): 
    class Gender(models.TextChoices):
        Man = 'male'
        Woman =  'female'  
    image=models.ImageField(upload_to='images/animals', blank=True, null=True)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    shelter=models.ForeignKey(Shelter, on_delete=models.CASCADE) 
    breed=models.CharField(max_length=100) 
    gender=models.CharField(max_length=10,choices=Gender.choices,default=Gender.Man)
    birthdate=models.DateField()
    description=models.TextField()
    weight=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



