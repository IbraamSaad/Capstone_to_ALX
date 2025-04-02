from django.urls import path
from . views import ViewsDocuments, ViewsProjects

urlpatterns = [
    path('project/', ViewsDocuments, name='project'),
    path('documet/', ViewsProjects, name='document'),
]