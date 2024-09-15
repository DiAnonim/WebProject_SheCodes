from django.contrib import admin
from app.models import CustomUser, Shelter, Comment,Animal,University,Mentor,CategoryAnimal,CategoryPost

admin.site.register(CustomUser)
admin.site.register(Shelter)
admin.site.register(Comment)
admin.site.register(Animal)
admin.site.register(University)
admin.site.register(Mentor)
admin.site.register(CategoryAnimal)
admin.site.register(CategoryPost)
