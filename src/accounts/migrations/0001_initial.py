# Generated by Django 3.0.6 on 2020-05-06 07:57

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_number', models.CharField(blank=True, max_length=127, null=True)),
                ('real_name', models.CharField(blank=True, max_length=127, null=True)),
                ('timezone', models.CharField(blank=True, max_length=127, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'User Profiles',
                'db_table': 'tbl_userprofile',
            },
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_period', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity Period',
                'verbose_name_plural': 'User Activity Periods',
                'db_table': 'tbl_activity_period',
            },
        ),
    ]
