# Generated by Django 4.0.5 on 2022-07-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_remove_register_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
