# Generated by Django 4.1.7 on 2023-04-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_alter_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='discount'),
        ),
    ]
