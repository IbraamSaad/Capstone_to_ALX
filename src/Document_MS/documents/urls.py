from django.urls import path
from .views import SignupViews, ProjectListView, DocumentsListView
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('welcome/', views.welcoming, name='welcome'),
    path('signup/', SignupViews.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='documents/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='documents/logout.html'), name='logout'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('documents/', DocumentsListView.as_view(), name='documents'),
    path('api/createuser/', views.CustomeUserListCreateAPIView.as_view(), name='user_create'),
    path('retrieveuser/<int:pk>/', views.CustomeUserRetrieveUpdateDelete.as_view(), name='retrieve_user'),
    path('api/createproject/', views.ProjectNameListCreateAPIView.as_view(), name='create_project'),
    path('retrieveproject/<int:pk>/', views.ProjectNameRetrieveUpdateDelete.as_view(), name='retrieve_project'),
    path('api/createdocumets/', views.DocumentsListCreateAPIView.as_view(), name='create_documents'),
    path('retrievedocumets/<int:pk>/', views.DocumentsRetrieveUpdateDelete.as_view(), name='retrieve_documents'),
]