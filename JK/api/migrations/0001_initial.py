# Generated by Django 4.1.7 on 2023-03-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.ImageField(upload_to='')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
