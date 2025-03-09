from django.db import models

# Create your models here.
class Projects(models.Model):
	project_name = models.CharField(max_length=200, blank=False, null=True)
	project_code = models.CharField(max_length=10, verbose_name='code', default='UNKNOWN')
	infraStructure_or_Constructions = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.project_name


class Documents(models.Model):
	discipline = [('ARCH', 'Architectural'), ('CI', 'Civil'), ('ME', 'Mechanical'), ('ELE', 'Electrical'),
	]

	d_type = [
	('DWD', 'Drawings'), ('RFI', 'Request for Information'), ('SUB', 'Submittals'), ('EIR', 'External Inspection Request'),
	]

	action = [
	('A', 'Approved'), ('B', 'Approved with Comments'), ('C', 'Revice and resumit'), ('D', 'Rejected'),
	]


	project = models.ForeignKey(Projects, on_delete=models.CASCADE)
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

	def __str__(self):
		return f"{self.documents_metaData} and {self.revision}"

