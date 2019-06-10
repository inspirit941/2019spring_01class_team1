# Generated by Django 2.1.2 on 2019-06-10 15:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cate', models.CharField(blank=True, max_length=2)),
                ('corporation', models.CharField(blank=True, max_length=255, verbose_name='corporation')),
                ('pid', models.CharField(blank=True, max_length=30, verbose_name='pid')),
                ('sid', models.CharField(blank=True, max_length=255, verbose_name='sid')),
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
            name='Product',
            fields=[
                ('classes', models.CharField(default=None, max_length=100, null=True)),
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.CharField(blank=True, max_length=255, null=True)),
                ('pname', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=100)),
                ('measurement', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('madefrom', models.CharField(default=None, max_length=100)),
                ('madein', models.CharField(default=None, max_length=100)),
                ('date_of_production', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('quality_gurantee', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('size', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('shoulder', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('chest', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('sleeve_len', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('sleeve_end', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('armpit', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('top_size', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('waist', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('thigh', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('bottom', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('crotch', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('tail', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('down_size', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('shoes_size', models.FloatField(blank=True, default=None, null=True)),
                ('ball_foot', models.FloatField(blank=True, default=None, null=True)),
                ('insole', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('heel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('front_heel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('shoes_height', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MD',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('management.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RS',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('management.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
