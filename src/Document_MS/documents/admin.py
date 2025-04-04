from django.contrib import admin
from . models import CustomUser, ProjectName, Documents

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ProjectName)
admin.site.register(Documents)