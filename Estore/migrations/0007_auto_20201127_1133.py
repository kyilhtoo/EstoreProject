# Generated by Django 3.1.3 on 2020-11-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0006_auto_20201127_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='media/%Y/%m/%d'),
        ),
    ]