# Generated by Django 3.2.4 on 2021-07-04 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210619_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='ISBN',
            new_name='isbn',
        ),
    ]
