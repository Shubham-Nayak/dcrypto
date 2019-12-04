# Generated by Django 2.2.3 on 2019-08-26 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rajarancho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldata',
            name='name',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alldata',
            name='finder',
            field=models.CharField(max_length=500),
        ),
    ]