# Generated by Django 3.0.6 on 2021-08-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210820_1447'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]