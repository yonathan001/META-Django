# Generated by Django 5.1.6 on 2025-03-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
