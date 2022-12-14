# Generated by Django 4.1.1 on 2022-10-16 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('user_type', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('going_from', models.CharField(max_length=255)),
                ('going_to', models.CharField(max_length=255)),
                ('date_time', models.CharField(max_length=35)),
                ('preferred_medium', models.CharField(blank=True, max_length=255, null=True)),
                ('assets_quantity', models.IntegerField()),
                ('assets_type', models.IntegerField()),
                ('assest_sensitivity', models.IntegerField()),
                ('delivered_to', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accepted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apis.user')),
            ],
        ),
        migrations.CreateModel(
            name='RideInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('going_from', models.CharField(max_length=255)),
                ('going_to', models.CharField(max_length=255)),
                ('date_time', models.CharField(max_length=35)),
                ('travel_medium', models.CharField(max_length=255)),
                ('assets_quantity', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apis.user')),
            ],
        ),
    ]
