# Generated by Django 4.1.7 on 2023-05-25 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.PositiveIntegerField(choices=[('S', 'sales'), ('R', 'rent')], max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=6)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garages_number', models.PositiveIntegerField()),
            ],
        ),
    ]
