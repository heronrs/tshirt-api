# Generated by Django 2.0.1 on 2018-01-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=3)),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
