# Generated by Django 4.0.6 on 2022-07-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_propertyproductblog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyproductblog',
            name='image',
            field=models.ImageField(upload_to='../upload'),
        ),
    ]
