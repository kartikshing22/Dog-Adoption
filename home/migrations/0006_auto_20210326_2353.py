# Generated by Django 3.1.1 on 2021-03-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210316_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Doberman', 'Doberman'), ('Stay_Dog', 'Stray dog'), ('German Shepherd', 'German Shepherd'), ('American Bully', 'American bully'), ('Pitbull', 'Pitbull'), ('Golden Retriever', 'Golden retriever'), ('Labrador_Retriever', 'Labrador Retriever'), ('French Bulldog', 'French Bulldog'), ('Bulldog', 'Bulldog'), ('Beagle', 'Beagle'), ('Poodle', 'Poodle'), ('Rottweiler', 'Rottweiler'), ('Yorkshire_Terrier', 'Yorkshire Terrier')], default='Doberman', max_length=50),
        ),
    ]
