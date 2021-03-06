# Generated by Django 3.1.5 on 2021-01-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='From2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=25)),
                ('last', models.CharField(blank=True, max_length=25)),
                ('father_name', models.CharField(blank=True, max_length=25)),
                ('mother_name', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('address', models.CharField(blank=True, max_length=55)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('number', models.CharField(max_length=10)),
                ('number1', models.CharField(max_length=12)),
                ('number2', models.CharField(max_length=14)),
            ],
        ),
    ]
