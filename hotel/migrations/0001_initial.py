# Generated by Django 4.1.5 on 2023-01-26 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('car_parking', models.BooleanField(default=False)),
                ('bike_parking', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('pick_up', models.BooleanField(default=False)),
                ('bed_breakfast', models.BooleanField(default=False)),
                ('launch', models.BooleanField(default=False)),
                ('party_area', models.BooleanField(default=False)),
                ('hotel_type', models.CharField(choices=[('GUESTHOUSE', 'Guesthouse'), ('HOMESTAY', 'Homestay'), ('RESORT', 'Resort')], max_length=50)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('check_in_time', models.TimeField()),
                ('check_out_time', models.TimeField()),
                ('images', models.TextField(max_length=16383, null=True)),
                ('video', models.TextField(max_length=16383, null=True)),
            ],
        ),
    ]