# Generated by Django 3.0.8 on 2020-07-12 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200712_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_type',
            new_name='phone',
        ),
    ]