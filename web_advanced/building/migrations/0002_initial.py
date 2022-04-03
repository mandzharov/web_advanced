# Generated by Django 4.0.3 on 2022-03-21 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building.building'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
