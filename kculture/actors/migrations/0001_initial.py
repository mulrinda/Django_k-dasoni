# Generated by Django 2.1.15 on 2020-07-23 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=500)),
                ('actor_img', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drama_name', models.CharField(max_length=500)),
                ('drama_img', models.CharField(max_length=500)),
                ('drama_cnt', models.ManyToManyField(null=True, related_name='user_drama', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='drama_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='actors.Drama'),
        ),
        migrations.AddField(
            model_name='actor',
            name='showman_cnt',
            field=models.ManyToManyField(null=True, related_name='user_actor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actor',
            name='spot_cd',
            field=models.ManyToManyField(null=True, related_name='spot_actor', to='maps.Spot'),
        ),
    ]
