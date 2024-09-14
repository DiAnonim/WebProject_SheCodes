from django.urls import path
from .views import *

urlpatterns = [
    path('', SignUpView.as_view(), name='home'),  
    path('message/', MessageView.as_view(), name='message'),
    # path('error/', ErrorView.as_view(), name='error'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('user/update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('user/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('profile/detail/<int:pk>/', ProfileView.as_view(), name='profile'),
    
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
]
