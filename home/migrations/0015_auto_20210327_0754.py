# Generated by Django 3.1.1 on 2021-03-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210327_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Doberman', 'Doberman'), ('Pitbull', 'Pitbull'), ('Bulldog', 'Bulldog'), ('Beagle', 'Beagle'), ('Poodle', 'Poodle'), ('Rottweiler', 'Rottweiler'), ('Yorkshire_Terrier', 'Yorkshire Terrier')], default='Doberman', max_length=50),
        ),
    ]
