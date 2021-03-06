# Generated by Django 3.2.5 on 2021-07-19 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('mobno', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('burg_type', models.CharField(choices=[('BK fried chicken', 'BK fried chicken'), ('Friends combo', 'Friends combo'), ('Family combo', 'Family combo'), ('Chiken Wings', 'Chiken Wings')], max_length=50)),
                ('burg_image', models.ImageField(upload_to='images/')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=30)),
                ('order_date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
