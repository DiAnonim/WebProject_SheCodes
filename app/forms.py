from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import CustomUser, Shelter, Comment
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

        
class LoginForm(AuthenticationForm):
    captcha = CaptchaField(label='', error_messages={'invalid': 'Неверная капча'})
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ""
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Username/Логин'})
        
        self.fields['password'].label = ""
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': 'Пароль'})
        
        self.fields['captcha'].widget.attrs.update({'class': 'inputCreate', 'placeholder': 'Введите капчу'})

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
        
        
    
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['image', 'title', 'text', 'datecompleted', 'important', 'status', 'perform']
#         labels = {
#             'image': '',
#             'title': '',
#             'text': '',
#             'datecompleted': '',
#             'important': '',
#             'status': '',
#             'perform': '',
#         }
#         widgets = {
#             'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
#             'title': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Заголовок'}),
#             'text': forms.Textarea(attrs={'class': 'inputCreate', 'placeholder': 'Описание'}),
#             'datecompleted': forms.DateInput(attrs={'type': 'date', 'class': 'inputCreate', 'placeholder': 'Дата выполнения'}),
#             'important': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Важность'}),
#             'status': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Статус'}),
#             'perform': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Выполнено'}),
#         }