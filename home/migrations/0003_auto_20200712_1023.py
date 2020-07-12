# Generated by Django 3.0.8 on 2020-07-12 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Address'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='index/images'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='', upload_to='index/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='index/images'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(default='', upload_to='index/images'),
        ),
    ]