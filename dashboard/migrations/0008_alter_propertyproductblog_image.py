# Generated by Django 4.0.6 on 2022-07-07 19:41

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_propertyproductblog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyproductblog',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='upload', location='upload'), upload_to='upload'),
        ),
    ]
