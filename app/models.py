from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # class Role(models.TextChoices):
    #     Admin = 'Admin'
    #     Director = 'Director'
    #     User = 'User'
    class Gender(models.TextChoices):
        Man = 'Man'
        Woman =  'Woman'  
    image=models.ImageField(upload_to='media/users',default="media/users/default.png")
    gender=models.CharField(max_length=10,choices=Gender.choices,default=Gender.Man)
    birthday=models.DateField(null=True)
    phone=models.CharField(max_length=20)
    isStudent = models.BooleanField(default=False)
    # role = models.CharField(max_length=50, choices=Role.choices, default=Role.User)

    def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
            return super().save(*args, **kwargs)
        
        
class CategoryPost(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "CategoryPost"
        verbose_name_plural = "CategoryPos"
        ordering = ['-created_at']

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/posts', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE, related_name='posts', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']
  
class Shelter(models.Model):
    image=models.ImageField(upload_to='media/shelters', blank=True, null=True)
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

class University(models.Model):
    image=models.ImageField(upload_to='images/university', blank=True, null=True)
    name = models.TextField()
    website =models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        ordering = ['-created_at']

class Mentor(models.Model):
    image=models.ImageField(upload_to='images/mentor', blank=True, null=True)
    name = models.TextField()
    surname = models.TextField()
    email= models.EmailField()
    typeOfActivity = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentors"
        ordering = ['-created_at']



class CategoryAnimal(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "CategoryAnimal"
        verbose_name_plural = "CategoryAnimals"
        ordering = ['-created_at']
    
class Animal(models.Model): 
    class Gender(models.TextChoices):
        Man = 'male'
        Woman =  'female'  
    image=models.ImageField(upload_to='media/animals', blank=True, null=True)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(CategoryAnimal, on_delete=models.CASCADE)
    categoryPost=models.ForeignKey(CategoryPost, on_delete=models.CASCADE)
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

