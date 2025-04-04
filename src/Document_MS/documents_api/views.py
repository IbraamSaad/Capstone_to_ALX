from . serializers import  SerialzerCustomeUser, SerializerProjectName, SerializerDocuments
from rest_framework.response import Response
from rest_framework import generics, status
from documents.models import CustomUser, ProjectName, Documents
from . permissions import IsAdminUserOrReadOnly
import logging


logger = logging.getLogger(__name__)

# Customizing List and Create API views for CutomeUser Serialization
class CustomeUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerialzerCustomeUser
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Customizing Retrieve, Update and Delete API views for CutomeUser Serialization
class CustomeUserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerialzerCustomeUser
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            logger.warning(f"User with pk={kwargs['pk']} not found.")
            return Response({'errors': {'detail': 'User not found'}}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving user: {e}", exc_info=True)
            return Response({'errors': {'detail': 'Internal server error'}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True) # partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Customizing API views for ProjectName Serialization
class ProjectNameListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectName.objects.all()
    serializer_class = SerializerProjectName
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Customizing Retrieve, Update and Delete API views for ProjectName Serialization
class ProjectNameRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectName.objects.all()
    serializer_class = SerializerProjectName
    permission_classes = [IsAdminUserOrReadOnly]

    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except ProjectName.DoesNotExist:
            logger.warning(f"Project with pk={kwargs['pk']} not found.")
            return Response({'errors': {'detail': 'Project not found'}}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving project: {e}", exc_info=True)
            return Response({'errors': {'detail': 'Internal server error'}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
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
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Customizing Retrieve, Update and Delete API views for Documents Serialization
class DocumentsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = SerializerDocuments
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Documents.DoesNotExist:
            logger.warning(f"Document with pk={kwargs['pk']} not found.")
            return Response({'errors': {'detail': 'Document not found'}}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving document: {e}", exc_info=True)
            return Response({'errors': {'detail': 'Internal server error'}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        logger.warning(f"Bad Request: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # filtering
    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
    

