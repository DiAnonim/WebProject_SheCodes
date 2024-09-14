from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

# from app.models import Todo, Comment
from app.forms import UserForm, LoginForm, ShelterForm,AnimalForm,UniversityForm,MentorForm,CategoryAnimalForm,CategoryPostForm
from app.models import CustomUser, Shelter,Animal,University,Mentor,CategoryAnimal,CategoryPost

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


# Вход, выход и регистрация
class SignUpView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "signup.html"
    success_url = reverse_lazy('message')
    succses_message = 'User created successfully. Now you can login'
    
    # def send_verification_email(self, user):
    #     token = default_token_generator.make_token(user)
    #     link = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
    #     subject = 'Verify your email'
    #     body = f"Hello {user.username}! \nPlease, confirm your email by clicking on the link below: \n{link}"
    #     send_mail(
    #         subject, body, 'd1anonim.555@gmail.com', [user.email], fail_silently=False)
        
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     user = self.object  
    #     user.is_active = False
    #     user.save()
    #     self.send_verification_email(self.object)
    #     return response
    

# class VerifyEmailView(View):
#     def get(self, request, pk, token):
#         user = CustomUser.objects.get(pk=pk)
#         if default_token_generator.check_token(user, token):
#             user.is_active = True
#             user.save()
#             messages.success(request, 'Your email has been verified')
#             return redirect('login')
#         else:
#             messages.error(request, 'Invalid verification link')
#             return redirect('home')
    
class LoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm 
    template_name = 'login.html'
    next_page = reverse_lazy('message')
    success_message = 'Login successfully'

class LogoutView(LogoutView):
    next_page = reverse_lazy('home')
    

    
# Сообщение
class MessageView(TemplateView):
    template_name = "message.html"
    
    
# Ошибка
class ErrorView(TemplateView):
    template_name = "error.html"


# Профиль
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = "user"
    
    
class ShelterCreateView(LoginRequiredMixin, CreateView):
    model = Shelter
    form_class = ShelterForm
    template_name = "create_shelter.html"
    success_url = reverse_lazy('message')
    success_message = 'Shelter created successfully'
    
class ShelterDetailView(LoginRequiredMixin, DetailView):
    model = Shelter
    template_name = "shelter_detail.html"
    context_object_name = "shelter"
    
class ShelterUpdateView(LoginRequiredMixin, UpdateView):
    model = Shelter
    form_class = ShelterForm
    template_name = "update_shelter.html"
    success_url = reverse_lazy('message')
    
class ShelterDeleteView(LoginRequiredMixin, DeleteView):
    model = Shelter
    template_name = "delete_shelter.html"
    success_url = reverse_lazy('message')

class MainView(TemplateView):
    template_name = "admin/main.html"
#Животные 
class AnimalCreateView(CreateView):
    model = Animal 
    form_class = AnimalForm
    template_name = "create_animal.html"
    success_url = reverse_lazy('message')
    success_message = 'Animal created successfully'

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = "delete_animal.html"
    success_url = reverse_lazy('message')

class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = "update_animal.html"
    form_class = AnimalForm
    success_url = reverse_lazy('message')

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "animal_detail.html"
    context_object_name = "animal"

#Университеты
class UniversityListView(ListView):
    model = University
    template_name = "admin/university.html"
    context_object_name = "universities"


class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityForm
    template_name = "create_university.html"
    success_url = reverse_lazy('message')
    success_message = 'University created successfully'

class UniversityDeleteView(DeleteView):
    model = University
    template_name = "delete_university.html"
    success_url = reverse_lazy('message')

class UniversityUpdateView(UpdateView):
    model = University
    template_name = "update_university.html"
    form_class = UniversityForm
    success_url = reverse_lazy('message')

class UniversityDetailView(DetailView):
    model = University
    template_name = "university_detail.html"
    context_object_name = "university"

#Менторы
class MentorCreateView(CreateView):
    model = Mentor
    form_class = MentorForm
    template_name = "create_mentor.html"
    success_url = reverse_lazy('message')
    success_message = 'Mentor created successfully'

class MentorDeleteView(DeleteView):
    model = Mentor
    template_name = "delete_mentor.html"
    success_url = reverse_lazy('message')

class MentorUpdateView(UpdateView):
    model = Mentor
    form_class = MentorForm
    template_name = "update_mentor.html"
    success_url = reverse_lazy('message')

class MentorDetailView(DetailView):
    model = Mentor
    template_name = "mentor_detail.html"
    context_object_name = "mentor"

class CategoryAnimalCreateView(CreateView):
    model = CategoryAnimal
    form_class = CategoryAnimalForm
    template_name = "create_category_animal.html"
    success_url = reverse_lazy('message')
    success_message = 'Category created successfully'

class CategoryAnimalDeleteView(DeleteView):
    model = CategoryAnimal
    template_name = "delete_category_animal.html"
    success_url = reverse_lazy('message')

class CategoryAnimalUpdateView(UpdateView):
    model = CategoryAnimal
    form_class = CategoryAnimalForm
    template_name = "update_category_animal.html"
    success_url = reverse_lazy('message')

class CategoryAnimalDetailView(DetailView):
    model = CategoryAnimal
    template_name = "category_animal_detail.html"
    context_object_name = "category_animal"
#
# # Задачи в home
# class TodoHomeView(ListView):
#     model = Todo
#     form_class = TodoForm
#     template_name = "home.html"
#     context_object_name = "todos"
#     paginate_by = 6

# class TodoCreateView(LoginRequiredMixin, SuccessMessageMixin,  CreateView):
#     model = Todo
#     form_class = TodoForm
#     template_name = "create_todo.html"
#     success_url = reverse_lazy('home')
#     success_message = 'Task created successfully'
    
#     def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)
   
   
# class TodoDetailView(LoginRequiredMixin, DetailView):
#     model = Todo
#     template_name = "todo_detail.html"
#     context_object_name = "todo"


# class TodoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = Todo
#     template_name = "delete_todo.html"
#     success_url = reverse_lazy('home')
#     success_message = 'Task deleted successfully'

# class TodoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Todo
#     form_class = TodoForm
#     template_name = "update_todo.html"
#     success_url = reverse_lazy('home')
#     success_message = 'Task updated successfully'
    
    
