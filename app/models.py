from django.db import models
class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        Man = 'Man'
        Woman =  'Woman'  
    Image=models.ImageField(upload_to='user/',default="user/")
    gender=models.CharField(max_length=10,choices=Gender.choices,default=Gender.Man)
    phone=models.CharField(max_length=20)
  
# Create your models here.
class Shelter(models.Model):
    image=models.ImageField(upload_to='images/shelter', blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Shelter"
        verbose_name_plural = "Shelters"
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-created_at']
    
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
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"
        ordering = ['-created_at']

class Comment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE,related_name="comments",verbose_name="Animal")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name="Author", related_name="comments")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']
    
class SavePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

