# Generated by Django 3.1.3 on 2020-11-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0005_auto_20201127_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='product_images/%Y/%m/%d'),
        ),
    ]
