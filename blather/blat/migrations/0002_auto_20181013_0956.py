# Generated by Django 2.0.4 on 2018-10-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blat',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]