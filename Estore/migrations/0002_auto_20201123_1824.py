# Generated by Django 3.1.3 on 2020-11-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
