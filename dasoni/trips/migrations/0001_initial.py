# Generated by Django 2.1.15 on 2020-08-15 07:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=500)),
                ('post_content', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_img', models.ImageField(upload_to='media')),
                ('post_user', models.ManyToManyField(null=True, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_user', models.ManyToManyField(null=True, related_name='tour_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
