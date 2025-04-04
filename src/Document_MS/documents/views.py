from django.shortcuts import render, redirect
from . models import ProjectName, Documents, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
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
                return redirect('login')  
            else:
                form.add_error(None, 'Invalid username or password') #  error message
        return render(request, self.template_name, {'form': form})
    
class LogoutView(View):
    template_name = 'documents/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('logout')  

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('logout')


# allow staff only ro create instances of Projects objects    
class ProjectNameCreateView(CreateView):
    model = ProjectName
    fields = '__all__'  
    template_name = 'documents/create_project.html'
    success_url = reverse_lazy('project_create') 

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Only admin users can create projects.")
        return super().dispatch(request, *args, **kwargs)

# permission required for listing projects
class ProjectListView(LoginRequiredMixin, ListView): # PermissionRequiredMixin
    model = ProjectName
    template_name = 'documents/list_project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter()
        return queryset
    
# allow staff only ro create instances of Documets objects 
class DocumetsCreateView(CreateView):
    model = ProjectName
    fields = '__all__'  
    template_name = 'documents/create_documents.html'
    success_url = reverse_lazy('documents_create') 

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Only admin users can create documents.")
        return super().dispatch(request, *args, **kwargs)

# permission required for listing documents    
class DocumentsListView(ListView, LoginRequiredMixin): # PermissionRequiredMixin
    model = Documents
    template_name = 'documents/list_documets.html'
    context_object_name = 'documents'
    #  filter object
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter()







         
        



