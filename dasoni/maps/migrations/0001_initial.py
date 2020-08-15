# Generated by Django 2.1.15 on 2020-08-15 04:19

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
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_name', models.CharField(max_length=500)),
                ('spot_address', models.CharField(max_length=500)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('spot_info', models.CharField(max_length=500)),
                ('spot_img', models.CharField(max_length=500)),
                ('spot_stamp', models.ManyToManyField(null=True, related_name='spot_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=500)),
                ('actor_img', models.CharField(max_length=500)),
                ('theme_img', models.CharField(max_length=500)),
                ('spot_cd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.Spot')),
            ],
        ),
    ]
