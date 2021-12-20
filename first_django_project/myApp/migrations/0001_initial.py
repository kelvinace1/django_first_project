# Generated by Django 3.2.9 on 2021-12-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200, unique=True)),
                ('l_name', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
