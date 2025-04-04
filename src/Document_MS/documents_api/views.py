from django.shortcuts import render, redirect
from . serializers import  SerialzerCustomeUser, SerializerProjectName, SerializerDocuments
from rest_framework.response import Response
from rest_framework import generics
from documents.models import CustomUser, ProjectName, Documents


# Create your views here.
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