from django.urls import path
from .views import *

urlpatterns = [
    path('', SignUpView.as_view(), name='home'),  
    path('message/', MessageView.as_view(), name='message'),
    # path('error/', ErrorView.as_view(), name='error'),
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/detail/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('verify/<int:pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    
    path('shelter/create/', ShelterCreateView.as_view(), name='create_shelter'),
    path('shelter/detail/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('shelter/update/<int:pk>/', ShelterUpdateView.as_view(), name='shelter_update'),
    path('shelter/delete/<int:pk>/', ShelterDeleteView.as_view(), name='shelter_delete'),
    
    path('admin/home',MainView.as_view(), name='admin_home'),
    path('admin/university/', UniversityListView.as_view(), name='university'),
    
    # path('todo/create', TodoCreateView.as_view(), name='create_todo'),
    # path('todo/detail/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    # path('todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'),
    # path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete'),
]
