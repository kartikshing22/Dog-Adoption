# Generated by Django 3.1.1 on 2021-04-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210401_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
