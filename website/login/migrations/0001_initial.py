# Generated by Django 4.1.7 on 2023-02-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=10)),
            ],
        ),
    ]
