from django.shortcuts import render, redirect
from . models import ProjectName, Documents
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView

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

         
        



