# Generated by Django 3.1.3 on 2020-11-28 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0009_additionalimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalimages',
            options={'verbose_name_plural': 'images'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]