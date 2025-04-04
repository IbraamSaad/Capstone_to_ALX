from rest_framework import serializers
from documents.models import CustomUser, ProjectName, Documents

class SerialzerCustomeUser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class SerializerProjectName(serializers.ModelSerializer):
    class Meta:
        model = ProjectName
        fields = '__all__'

class SerializerDocuments(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'