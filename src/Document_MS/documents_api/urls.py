"""
URL configuration for Document_MS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from documents_api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # User API endpoints
    path('api/users/', views.CustomeUserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', views.CustomeUserRetrieveUpdateDelete.as_view(), name='user-detail'),

    # Project API endpoints
    path('api/projects/', views.ProjectNameListCreateAPIView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', views.ProjectNameRetrieveUpdateDelete.as_view(), name='project-detail'),

    # Document API endpoints
    path('api/documents/', views.DocumentsListCreateAPIView.as_view(), name='document-list-create'),
    path('api/documents/<int:pk>/', views.DocumentsRetrieveUpdateDelete.as_view(), name='document-detail'),
]
# 