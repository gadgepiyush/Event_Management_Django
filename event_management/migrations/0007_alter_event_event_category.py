# Generated by Django 4.1.1 on 2022-11-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0006_ticket_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('Social Event', 'Social Event'), ('Concert', 'Concert'), ('Music Show', 'Music Show'), ('Movie Show', 'Movie Show'), ('Charity Event', 'Charity Event'), ('Comedy Show', 'Comedy Show')], max_length=30),
        ),
    ]