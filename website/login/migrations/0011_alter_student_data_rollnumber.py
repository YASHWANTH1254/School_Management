# Generated by Django 4.1.7 on 2023-03-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_teacher_performance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='RollNumber',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]