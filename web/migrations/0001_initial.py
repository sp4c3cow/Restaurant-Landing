# Generated by Django 3.1.3 on 2020-11-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=16)),
                ('date_reservation', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('num_of_people', models.IntegerField(max_length=2)),
                ('message', models.TextField(max_length=600)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
