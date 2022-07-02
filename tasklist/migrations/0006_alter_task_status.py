# Generated by Django 4.0.3 on 2022-07-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'COMPLETED'), ('pending', 'PENDING')], default='P', max_length=20),
        ),
    ]