from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View

from app.forms import UserForm, LoginForm, ShelterForm,AnimalForm,UniversityForm,MentorForm,\
                        CategoryAnimalForm,CategoryPostForm, CommentForm, UpdateUserForm

from app.models import CustomUser, Shelter,Animal,University,Mentor,CategoryAnimal,CategoryPost, Comment

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
    
    
class LoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm 
    template_name = 'login.html'
    next_page = reverse_lazy('message')
    success_message = 'Login successfully'
    
    
# Профиль
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = "user"
    
    def get_object(self):
        return self.request.user
    
class UpdateUserView(UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'update_user.html'

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.kwargs['pk'])
    
    
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('message')
    success_message = 'Profile deleted successfully'
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    

    
# Сообщение
class MessageView(TemplateView):
    template_name = "message.html"
    
    
# Ошибка
class ErrorView(TemplateView):
    template_name = "error.html"

    
    
# CRUD для комментариев
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "comment_list.html"
    context_object_name = "comments"
    paginate_by = 5

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "create_comment.html"
    success_url = reverse_lazy('message')
    success_message = 'Comment created successfully'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "update_comment.html"
    success_url = reverse_lazy('message')
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_comment.html"
    success_url = reverse_lazy('message')
    
    
    
    
    






    
   
# CRUD для комментариев
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "comment_list.html"
    context_object_name = "comments"
    paginate_by = 5

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "create_comment.html"
    success_url = reverse_lazy('message')
    success_message = 'Comment created successfully'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "update_comment.html"
    success_url = reverse_lazy('message')
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_comment.html"
    success_url = reverse_lazy('message')




    
#Животные 
class AnimalListView(ListView):
    model = Animal
    template_name = "sectionAnimals/home.html"
    context_object_name = "animals"
    
    
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
    template_name = "customAdmin/university.html"
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
class MentorListView(ListView):
    model = Mentor
    template_name = "customAdmin/mentor.html"
    context_object_name = "mentors"

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

#Категории животных
class CategoryAnimalListView(ListView):
    model = CategoryAnimal
    template_name = "customAdmin/animalCategory.html"
    context_object_name = "category_animals"

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

#Post Category 
class PostCategoryListView(ListView):
    model = CategoryPost
    template_name = "customAdmin/postCategory.html"
    context_object_name = "post_categories"

class PostCategoryCreateView(CreateView):
    model = CategoryPost
    form_class = CategoryPostForm
    template_name = "create_category_post.html"
    success_url = reverse_lazy('message')
    success_message = 'Category created successfully'

class PostCategoryDeleteView(DeleteView):
    model = CategoryPost
    template_name = "delete_category_post.html"
    success_url = reverse_lazy('message')

class PostCategoryUpdateView(UpdateView):
    model = CategoryPost
    form_class = CategoryPostForm
    template_name = "update_category_post.html"
    success_url = reverse_lazy('message')

class PostCategoryDetailView(DetailView):
    model = CategoryPost
    template_name = "category_post_detail.html"
    context_object_name = "category_post"
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Admin
    
class MainView(ListView):
    model = CustomUser
    template_name = "customAdmin/main.html"
    context_object_name = "customusers"
    
#Животные 
class AnimalListViewAdmin(ListView):
    model = Animal
    template_name = "customAdmin/animal.html"
    context_object_name = "animals"
    
class AnimalCreateViewAdmin(CreateView):
    model = Animal 
    form_class = AnimalForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'Animal created successfully'

class AnimalDeleteViewAdmin(DeleteView):
    model = Animal
    template_name = "delete_animal.html"
    success_url = reverse_lazy('message')

class AnimalUpdateViewAdmin(UpdateView):
    model = Animal
    template_name = "update_animal.html"
    form_class = AnimalForm
    success_url = reverse_lazy('message')

class AnimalDetailViewAdmin(DetailView):
    model = Animal
    template_name = "animal_detail.html"
    context_object_name = "animal"

#Университеты
class UniversityListViewAdmin(ListView):
    model = University
    template_name = "customAdmin/university.html"
    context_object_name = "universities"


class UniversityCreateViewAdmin(CreateView):
    model = University
    form_class = UniversityForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'University created successfully'

class UniversityDeleteViewAdmin(DeleteView):
    model = University
    template_name = "delete_university.html"
    success_url = reverse_lazy('message')

class UniversityUpdateViewAdmin(UpdateView):
    model = University
    template_name = "update_university.html"
    form_class = UniversityForm
    success_url = reverse_lazy('message')

class UniversityDetailViewAdmin(DetailView):
    model = University
    template_name = "university_detail.html"
    context_object_name = "university"

#Менторы
class MentorListViewAdmin(ListView):
    model = Mentor
    template_name = "customAdmin/mentor.html"
    context_object_name = "mentors"

class MentorCreateViewAdmin(CreateView):
    model = Mentor
    form_class = MentorForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'Mentor created successfully'

class MentorDeleteViewAdmin(DeleteView):
    model = Mentor
    template_name = "delete_mentor.html"
    success_url = reverse_lazy('message')

class MentorUpdateViewAdmin(UpdateView):
    model = Mentor
    form_class = MentorForm
    template_name = "update_mentor.html"
    success_url = reverse_lazy('message')

class MentorDetailViewAdmin(DetailView):
    model = Mentor
    template_name = "mentor_detail.html"
    context_object_name = "mentor"

#Категории животных
class CategoryAnimalListViewAdmin(ListView):
    model = CategoryAnimal
    template_name = "customAdmin/animalCategory.html"
    context_object_name = "category_animals"

class CategoryAnimalCreateViewAdmin(CreateView):
    model = CategoryAnimal
    form_class = CategoryAnimalForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'Category created successfully'

class CategoryAnimalDeleteViewAdmin(DeleteView):
    model = CategoryAnimal
    template_name = "delete_category_animal.html"
    success_url = reverse_lazy('message')

class CategoryAnimalUpdateViewAdmin(UpdateView):
    model = CategoryAnimal
    form_class = CategoryAnimalForm
    template_name = "update_category_animal.html"
    success_url = reverse_lazy('message')

class CategoryAnimalDetailViewAdmin(DetailView):
    model = CategoryAnimal
    template_name = "category_animal_detail.html"
    context_object_name = "category_animal"

#Post Category 
class PostCategoryListViewAdmin(ListView):
    model = CategoryPost
    template_name = "customAdmin/postCategory.html"
    context_object_name = "post_categories"

class PostCategoryCreateViewAdmin(CreateView):
    model = CategoryPost
    form_class = CategoryPostForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'Category created successfully'

class PostCategoryDeleteViewAdmin(DeleteView):
    model = CategoryPost
    template_name = "delete_category_post.html"
    success_url = reverse_lazy('message')

class PostCategoryUpdateViewAdmin(UpdateView):
    model = CategoryPost
    form_class = CategoryPostForm
    template_name = "update_category_post.html"
    success_url = reverse_lazy('message')

class PostCategoryDetailViewAdmin(DetailView):
    model = CategoryPost
    template_name = "category_post_detail.html"
    context_object_name = "category_post"
# CRUD для приюта 
class ShelterListViewAdmin(ListView):
    model = Shelter
    template_name = "customAdmin/shelter.html"
    context_object_name = "shelters"
    

class ShelterCreateViewAdmin(LoginRequiredMixin, CreateView):
    model = Shelter
    form_class = ShelterForm
    template_name = "customAdmin/customAdminCreate.html"
    success_url = reverse_lazy('message')
    success_message = 'Shelter created successfully'
    
class ShelterDetailViewAdmin(LoginRequiredMixin, DetailView):
    model = Shelter
    template_name = "shelter_detail.html"
    context_object_name = "shelter"
    
class ShelterUpdateViewAdmin(LoginRequiredMixin, UpdateView):
    model = Shelter
    form_class = ShelterForm
    template_name = "update_shelter.html"
    success_url = reverse_lazy('message')
    
class ShelterDeleteViewAdmin(LoginRequiredMixin, DeleteView):
    model = Shelter
    template_name = "delete_shelter.html"
    success_url = reverse_lazy('message')
    
    
    
    
    
    
    
    
    