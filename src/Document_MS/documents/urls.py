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

]