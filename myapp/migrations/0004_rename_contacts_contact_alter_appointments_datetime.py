# Generated by Django 5.1.3 on 2024-11-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contacts',
            new_name='contact',
        ),
        migrations.AlterField(
            model_name='appointments',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
