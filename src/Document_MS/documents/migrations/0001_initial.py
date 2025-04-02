# Generated by Django 5.1.6 on 2025-04-02 14:12

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200, unique=True)),
                ('Project_Description', models.TextField(blank=True)),
                ('project_code', models.IntegerField(unique=True)),
                ('starting_date', models.DateField()),
                ('dueDate', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_namber', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_extension', models.FileField(upload_to='documents/')),
                ('documents_type', models.CharField(choices=[('DWD', 'Drawings'), ('RFI', 'Request for Information'), ('SUB', 'Submittals'), ('EIR', 'External Inspection Request')], default='UNKNOWN', max_length=20, verbose_name='d_type')),
                ('documents_metaData', models.CharField(max_length=50)),
                ('document_discpline_or_trade', models.CharField(choices=[('ARCH', 'Architectural'), ('CI', 'Civil'), ('ME', 'Mechanical'), ('ELE', 'Electrical')], max_length=15, verbose_name='discipline')),
                ('revision', models.CharField(default='rev00', max_length=20)),
                ('document_description', models.TextField(null=True)),
                ('issue_date', models.DateField()),
                ('recived_date', models.DateField()),
                ('submition', models.CharField(choices=[('A', 'Approved'), ('B', 'Approved with Comments'), ('C', 'Revice and resubmit'), ('D', 'Rejected')], max_length=20, verbose_name='action')),
                ('issuer', models.CharField(max_length=50)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documents.projectname')),
            ],
        ),
    ]
