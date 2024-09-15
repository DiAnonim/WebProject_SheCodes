from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import CustomUser, Shelter, Comment,Animal,University,Mentor ,CategoryAnimal,CategoryPost
from django import forms
from captcha.fields import CaptchaField

# from .models import Todo, Comment

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = ""
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Пароль', 'class': 'form-control'
        })
        
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = ""
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль', 'class': 'form-control'
        })

    class Meta:
        model = CustomUser
        
        fields = ['image','first_name', 'last_name', 'birthday', 'email', 'gender', 'phone', 'username', 'password1', 'password2', ]
        
        labels = {
            'image': '',
            'first_name': '',
            'last_name': '',
            'birthday': '',
            'email': '',
            'gender': '',
            'phone': '',
            'username': '',
        }
       
        help_texts = {
            'first_name': '',
            'last_name': '',
            'birthday': '',
            'email': '',
            'gender': '',
            'phone': '',
            'username': '',
        }
        
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Фото'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'placeholder': 'День рождения', 'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username/Логин', 'class': 'form-control'}),
        }


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': '',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username/Логин', 'class': 'form-control'}),
        }
        
        
        
class LoginForm(AuthenticationForm):
    captcha = CaptchaField(label='', error_messages={'invalid': 'Неверная капча'})
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ""
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Username/Логин'})
        
        self.fields['password'].label = ""
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': 'Пароль'})
        
        self.fields['captcha'].widget.attrs.update({'class': 'inputCreate', 'placeholder': 'Введите капчу'})
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal

        fields = ['image', 'name', 'category', 'shelter', 'breed', 'gender', 'birthdate']

        labels = {
            'image': '',
            'name': '',
            'category': '',
            'shelter': '',
            'breed': '',
            'gender': '',
            'birthdate': '',
        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
            'category': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Категория'}),
            'shelter': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Приют'}),
            'breed': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Порода'}),
            'gender': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Пол'}),
            'birthdate': forms.DateInput(attrs={'class': 'inputCreate', 'placeholder': 'День рождения', 'type': 'date'}),
        }
class UniversityForm(forms.ModelForm):
    class Meta:
        model = University

        fields = ['image', 'name', 'website', 'phone_number']

        labels = {
            'image': '',
            'name': '',
            'website': '',
            'phone_number': '',
       
        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
            'website': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Сайт'}),
            'phone_number': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Телефон'}),
            
        }

class CategoryAnimalForm(forms.ModelForm):
    class Meta:
        model = CategoryAnimal

        fields = ['name']

        labels = {
            'name': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
        }
class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor

        fields = ['image', 'name', 'surname', 'email', 'typeOfActivity', 'phone_number']

        labels = {
            'image': '',
            'name': '',
            'surname': '',
            'email': '',
            'typeOfActivity': '',
            'phone_number': '',
        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Имя'}),
            'surname': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'class': 'inputCreate', 'placeholder': 'Email'}),
            'typeOfActivity': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Тип активности'}),
            'phone_number': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Телефон'}),
        }


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        
        fields = ['image', 'name', 'address', 'city', 'phoneNumber', 'description']
        
        labels = {
            'image': '',
            'name': '',
            'address': '',
            'city': '',
            'phoneNumber': '',
            'description': '',
        }
        
        widgets = {
            'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
            'address': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Адрес'}),
            'city': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Город'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Телефон'}),
            'description': forms.Textarea(attrs={'class': 'inputCreate', 'placeholder': 'Описание'}),
        }

class CategoryPostForm(forms.ModelForm):
    class Meta:
        model = CategoryPost
        fields = ['name']

        labels = {
            'name': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
        }

class CategoryAnimalForm(forms.ModelForm):
    class Meta:
        model = CategoryAnimal
        fields = ['name']

        labels = {
            'name': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Название'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'inputCreate', 'placeholder': 'Текст комментария'}),
        }
        
    