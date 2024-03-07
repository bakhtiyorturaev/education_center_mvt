# Generated by Django 5.0.3 on 2024-03-07 11:29

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='media/default_project.jpg', upload_to='media/projects')),
                ('demo_link', models.CharField(blank=True, max_length=400, null=True)),
                ('source_link', models.CharField(blank=True, max_length=400, null=True)),
                ('vote_count', models.IntegerField(default=0)),
                ('vote_ratio', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profil')),
                ('tag', models.ManyToManyField(blank=True, related_name='project_tag', to='projects.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(default='')),
                ('value', models.CharField(choices=[('+', 'Ijobiy'), ('-', 'Salbiy')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_review', to='projects.project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profil')),
            ],
        ),
    ]
