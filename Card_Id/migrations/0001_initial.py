# Generated by Django 4.2.4 on 2023-09-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Virtual_Id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Emp_id', models.BigIntegerField()),
                ('Contact', models.BigIntegerField()),
                ('Designation', models.CharField(max_length=50)),
            ],
        ),
    ]
