# Generated by Django 2.0.7 on 2018-07-31 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180731_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSide',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'OrderSide',
                'verbose_name_plural': 'OrderSides',
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'OrderType',
                'verbose_name_plural': 'OrderTypes',
            },
        ),
    ]