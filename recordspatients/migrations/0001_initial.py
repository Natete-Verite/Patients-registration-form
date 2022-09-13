# Generated by Django 4.1.1 on 2022-09-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('diabetes', models.BooleanField()),
                ('no_diabetes', models.BooleanField()),
                ('unknown', models.BooleanField()),
            ],
        ),
    ]
