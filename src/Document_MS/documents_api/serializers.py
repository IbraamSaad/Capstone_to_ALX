from rest_framework import serializers
from documents.models import CustomUser, ProjectName, Documents
from django.core.validators import RegexValidator
from django.core import validators

class SerialzerCustomeUser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate_phone_number(self, phone_number):
        phone_regex = r'^\+?1?\d{9,15}$'
        if not validators.RegexValidator(regex=phone_regex).validate(phone_number):
            raise serializers.ValidationError("Phone number must be in this format: +999999999")
        return phone_number

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        # i could valdiate for more fields

        if first_name and last_name and first_name == last_name:
            raise serializers.ValidationError("First and last name cannot be the same.")

        return attrs
    
        
class SerializerProjectName(serializers.ModelSerializer):
    class Meta:
        model = ProjectName
        fields = '__all__'

class SerializerDocuments(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

    def validate(self, attrs):
        Documents_metadata = attrs.get("Documents_Metadata")
        zip_valditor = RegexValidator(
            regex=r'^\d{5}(?:-\d{4})?$',
            message="Code must be in format: XXX-XXX-XXX"
        )
        if Documents_metadata != zip_valditor:
            raise serializers.ValidationError(zip_valditor)
        return Documents_metadata