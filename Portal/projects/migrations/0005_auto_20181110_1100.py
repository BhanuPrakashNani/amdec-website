# Generated by Django 2.1.2 on 2018-11-10 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20181110_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='colors',
            new_name='colour',
        ),
    ]