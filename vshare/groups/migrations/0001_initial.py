# Generated by Django 3.0.3 on 2020-04-04 18:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('since', models.DateTimeField(auto_now_add=True)),
                ('groupid', models.CharField(default='', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('title', models.CharField(blank=True, default='No Name', max_length=100)),
                ('describtion', models.TextField(blank=True)),
                ('invite_only', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_group_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['since'],
            },
        ),
    ]