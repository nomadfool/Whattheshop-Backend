# Generated by Django 2.1.7 on 2019-04-07 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190402_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
