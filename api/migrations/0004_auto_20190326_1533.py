# Generated by Django 2.1.7 on 2019-03-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190326_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(to='api.Category'),
        ),
    ]
