# Generated by Django 4.2.4 on 2023-09-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0009_alter_items_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=55)),
                ('Type', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('UserId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=55)),
                ('Type', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('UserId', models.IntegerField()),
                ('Quantity', models.IntegerField()),
            ],
        ),
    ]
