from django.shortcuts import render, redirect
from . models import ProjectName, Documents, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from . serializers import  SerialzerCustomeUser, SerializerProjectName, SerializerDocuments
from rest_framework.response import Response
from rest_framework import generics

def welcoming(request):
    return render(request, 'documents/welcome.html')


class SignupViews(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'documents/signup.html'

class LoginView(View):
    template_name = 'documents/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_engine, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')  # Replace 'home' with your desired redirect URL
            else:
                form.add_error(None, 'Invalid username or password') # general error message
        return render(request, self.template_name, {'form': form})
    
class LogoutView(View):
    template_name = 'documents/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('logout')  # Replace 'home' with your desired redirect URL

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('logout')
    

class ProjectListView(ListView):
    model = ProjectName
    template_name = 'documents/list_project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter()
        return queryset
    
class DocumentsListView(ListView):
    model = Documents
    template_name = 'documents/list_documets.html'
    context_object_name = 'documents'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter()

# Customizing List and Create API views for CutomeUser Serialization
class CustomeUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerialzerCustomeUser
# Customizing Retrieve, Update and Delete API views for CutomeUser Serialization
class CustomeUserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerialzerCustomeUser

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Customizing API views for ProjectName Serialization
class ProjectNameListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectName.objects.all()
    serializer_class = SerializerProjectName

# Customizing Retrieve, Update and Delete API views for ProjectName Serialization
class ProjectNameRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectName.objects.all()
    serializer_class = SerializerProjectName
    
    # filtering
    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset

# Customizing API views for Documents Serialization
class DocumentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = SerializerDocuments

# Customizing Retrieve, Update and Delete API views for Documents Serialization
class DocumentsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = SerializerDocuments

    # filtering
    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset





         
        



