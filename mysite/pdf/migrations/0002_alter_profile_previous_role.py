# Generated by Django 5.0.3 on 2024-04-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='previous_role',
            field=models.TextField(max_length=1000),
        ),
    ]
