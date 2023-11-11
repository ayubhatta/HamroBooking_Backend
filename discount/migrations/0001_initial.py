# Generated by Django 4.1.7 on 2023-04-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')], max_length=50)),
                ('description', models.TextField()),
                ('banner', models.ImageField(upload_to='discount')),
                ('amount', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]