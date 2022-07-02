# Generated by Django 4.0.3 on 2022-07-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0004_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], default='P', max_length=20),
        ),
    ]