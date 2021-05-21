# Generated by Django 3.2.3 on 2021-05-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
