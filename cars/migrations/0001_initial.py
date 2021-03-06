# Generated by Django 3.2 on 2021-04-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
