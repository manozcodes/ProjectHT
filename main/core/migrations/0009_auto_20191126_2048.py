# Generated by Django 2.2.7 on 2019-11-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_destination_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='dest_category',
            field=models.BooleanField(choices=[('religious', 'Religious'), ('waterbody', 'Water Body'), ('adventure', 'Adventurous'), ('nature', 'Nature Seeing')], default='nature', max_length=100),
        ),
    ]
