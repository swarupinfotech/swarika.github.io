# Generated by Django 4.2.4 on 2023-08-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='Person',
            field=models.IntegerField(),
        ),
    ]
