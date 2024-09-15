from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  
    path('message/', MessageView.as_view(), name='message'),
    # path('error/', ErrorView.as_view(), name='error'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('user/update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('user/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('profile/detail/<int:pk>/', ProfileView.as_view(), name='profile'),
    
    path('animals/list/', AnimalListView.as_view(), name='animal_list'),
    path('animals/create/', AnimalCreateView.as_view(), name='create_animal'),
    path('animals/detail/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('animals/update/<int:pk>/', AnimalUpdateView.as_view(), name='animal_update'),
    path('animals/delete/<int:pk>/', AnimalDeleteView.as_view(), name='animal_delete'),
    path('library/', LibraryTemplateView.as_view(), name='library'),
    # path('verify/<int:pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),

    # path('shelter/create/', ShelterCreateView.as_view(), name='create_shelter'),
    # path('shelter/detail/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    # path('shelter/update/<int:pk>/', ShelterUpdateView.as_view(), name='shelter_update'),
    # path('shelter/delete/<int:pk>/', ShelterDeleteView.as_view(), name='shelter_delete'),


    # path('comment/list/', CommentListView.as_view(), name='comment_list'),
    # path('comment/create/', CommentCreateView.as_view(), name='create_comment'),
    # path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    # path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),

    path('customAdmin/home/',MainView.as_view(), name='admin_home'),
    path('customAdmin/university/', UniversityListViewAdmin.as_view(), name='admin_university_list'),
    path('customAdmin/mentor/', MentorListViewAdmin.as_view(), name='admin_mentor_list'),
    path('customAdmin/categoryanimal/', CategoryAnimalListViewAdmin.as_view(), name='admin_categoryanimal_list'),
    path('customAdmin/categorypost',PostCategoryListViewAdmin.as_view(), name='admin_categorypost_list'),
    path('customAdmin/shelter/', ShelterListViewAdmin.as_view(), name='admin_shelter_list'),
    path('customAdmin/animal/', AnimalListViewAdmin.as_view(), name='admin_animal_list'),
   
    #create
    path('customAdmin/university/create/', UniversityCreateViewAdmin.as_view(), name='admin_create_university'),
    path('customAdmin/mentor/create/', MentorCreateViewAdmin.as_view(), name='admin_create_mentor'),
    path('customAdmin/shelter/create/', ShelterCreateViewAdmin.as_view(), name='admin_create_shelter'),
    path('customAdmin/categoryanimal/create/', CategoryAnimalCreateViewAdmin.as_view(), name='admin_create_categoryanimal'),
    path('customAdmin/categorypost/create/', PostCategoryCreateViewAdmin.as_view(), name='admin_create_categorypost'),
    path('customAdmin/animal/create/', AnimalCreateViewAdmin.as_view(), name='admin_create_animal'),
    #update
    path('customAdmin/university/update/<int:pk>/', UniversityUpdateViewAdmin.as_view(), name='admin_update_university'),
    path('customAdmin/mentor/update/<int:pk>/', MentorUpdateViewAdmin.as_view(), name='admin_update_mentor'),
    path('customAdmin/shelter/update/<int:pk>/', ShelterUpdateViewAdmin.as_view(), name='admin_update_shelter'),
    path('customAdmin/animal/update/<int:pk>/', CategoryAnimalUpdateViewAdmin.as_view(), name='categoryadmin_update_animal'),
    path('customAdmin/categorypost/update/<int:pk>/', PostCategoryUpdateViewAdmin.as_view(), name='admin_update_categorypost'),
    path('customAdmin/animal/update/<int:pk>/', AnimalUpdateViewAdmin.as_view(), name='admin_update_animal'),
    # delete
    path('customAdmin/university/delete/<int:pk>/', UniversityDeleteViewAdmin.as_view(), name='admin_delete_university'),
    path('customAdmin/mentor/delete/<int:pk>/', MentorDeleteViewAdmin.as_view(), name='admin_delete_mentor'),
    path('customAdmin/shelter/delete/<int:pk>/', ShelterDeleteViewAdmin.as_view(), name='admin_delete_shelter'),
    path('customAdmin/categoryanimal/delete/<int:pk>/', CategoryAnimalDeleteViewAdmin.as_view(), name='admin_delete_categoryanimal'),
    path('customAdmin/categorypost/delete/<int:pk>/', PostCategoryDeleteViewAdmin.as_view(), name='admin_delete_categorypost'),
    path('customAdmin/animal/delete/<int:pk>/', AnimalDeleteViewAdmin.as_view(), name='admin_delete_animal'),
    

]
