from django.urls import path
from .views import SignupViews, ProjectListView, DocumentsListView, ProjectNameCreateView, DocumetsCreateView
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('welcome/', views.welcoming, name='welcome'),
    path('signup/', SignupViews.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='documents/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='documents/logout.html'), name='logout'),
    path('project_create/', ProjectNameCreateView.as_view(), name='project_create'),
    path('project_list/', ProjectListView.as_view(), name='project_list'),
    path('documents_create/', DocumetsCreateView.as_view(), name='documents_create'),
    path('documents_list/', DocumentsListView.as_view(), name='documents_list'),
    
]