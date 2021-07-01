# Generated by Django 3.2 on 2021-05-05 20:50

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
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('isAdmin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=50)),
                ('from_city', models.CharField(max_length=15)),
                ('to_city', models.CharField(max_length=15)),
                ('from_airport', models.CharField(max_length=50)),
                ('to_airport', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('landing_date', models.DateField()),
                ('landing_time', models.TimeField()),
                ('flight_duration', models.CharField(max_length=15)),
                ('economy_price', models.CharField(max_length=15)),
                ('business_price', models.CharField(max_length=15)),
                ('number_of_stops', models.IntegerField()),
                ('waiting_time', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('on_flight', models.ManyToManyField(related_name='flight', to='main.User')),
            ],
        ),
    ]
