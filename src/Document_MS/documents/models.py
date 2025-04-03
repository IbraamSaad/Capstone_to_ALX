from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_namber = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class ProjectName(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='assigned_project', null=True, blank=True)
    project_name = models.CharField(max_length=200, blank=False, unique=True)
    Project_Description = models.TextField(blank=True, unique=False)
    project_code = models.IntegerField(blank=False, unique=True)
    starting_date = models.DateField(blank=False, unique=False)
    dueDate = models.DurationField()
    def __str__(self):
        return self.project_name

class Documents(models.Model):
	discipline = [('ARCH', 'Architectural'), ('CI', 'Civil'), ('ME', 'Mechanical'), ('ELE', 'Electrical'),
	]

	d_type = [
	('DWD', 'Drawings'), ('RFI', 'Request for Information'), ('SUB', 'Submittals'), ('EIR', 'External Inspection Request'),
	]

	action = [
	('A', 'Approved'), ('B', 'Approved with Comments'), ('C', 'Revice and resubmit'), ('D', 'Rejected'),
	]


	project = models.OneToOneField(ProjectName, on_delete=models.CASCADE)
	document_extension = models.FileField(upload_to='documents/')
	documents_type = models.CharField(max_length=20, choices=d_type, verbose_name='d_type', default='UNKNOWN')
	documents_metaData = models.CharField(max_length=50)
	document_discpline_or_trade = models.CharField(max_length=15, verbose_name='discipline', choices=discipline)
	revision = models.CharField(max_length=20, default='rev00')
	document_description = models.TextField(blank=False, null=True)
	issue_date = models.DateField(blank=False)
	recived_date = models.DateField(blank=False)
	submition = models.CharField(max_length=20, choices=action, verbose_name='action')
	issuer = models.CharField(max_length=50)

	class meta:
		db_table = 'documents'
		ordering = ['documents_metaData', 'documents_type']

	def __str__(self):
		return f"{self.documents_metaData} and {self.revision}"

