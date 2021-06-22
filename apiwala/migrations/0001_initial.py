# Generated by Django 3.2.4 on 2021-06-21 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_student', models.CharField(max_length=40)),
                ('college_name', models.CharField(max_length=50)),
                ('year_of_study', models.IntegerField()),
                ('father_name', models.CharField(max_length=50)),
                ('course_enrolled', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_plan', models.BooleanField(default=True)),
                ('silver_plan', models.BooleanField(default=False)),
                ('gold_plan', models.BooleanField(default=False)),
                ('diamond_plan', models.BooleanField(default=False)),
                ('index', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100)),
                ('limit', models.CharField(default='50', max_length=10)),
                ('index', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_api_permission', models.BooleanField(default=False)),
                ('post_api_permission', models.BooleanField(default=False)),
                ('put_api_permission', models.BooleanField(default=False)),
                ('patch_api_permission', models.BooleanField(default=False)),
                ('delete_api_permission', models.BooleanField(default=False)),
                ('index', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
