# Generated by Django 4.2.4 on 2023-09-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Card_Id', '0003_alter_virtual_id_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtual_id',
            name='img',
            field=models.ImageField(blank='True', null='True', upload_to='Images'),
        ),
    ]
