# Generated by Django 4.1.1 on 2022-11-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('event_category', models.CharField(choices=[(1, 'Social Event'), (2, 'Concert'), (3, 'Music Show'), (4, 'Movie Show')], max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('available_seats', models.IntegerField()),
                ('ticket_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('username', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]