# Generated by Django 4.0.6 on 2022-07-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_brand_product_gender_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('s', 'S (27)'), ('m', 'M (18)'), ('l', 'L (0)'), ('xl', 'XL (1)'), ('xxl', 'XXL (2)')], default='m', max_length=6),
        ),
    ]
