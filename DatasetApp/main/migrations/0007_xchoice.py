# Generated by Django 4.2.1 on 2023-05-31 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_airpollution_lat_alter_airpollution_lng'),
    ]

    operations = [
        migrations.CreateModel(
            name='xChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('North America', 'North America'), ('Sorth America', 'South America'), ('Europe', 'Europe'), ('Asia', 'Asia'), ('Oceania', 'Oceania')], default='North America', max_length=20)),
            ],
        ),
    ]
