# Generated by Django 2.0.7 on 2018-07-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_orderside_ordertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biz',
            name='order_side',
            field=models.ForeignKey(on_delete=False, to='app.OrderSide'),
        ),
        migrations.AlterField(
            model_name='biz',
            name='order_type',
            field=models.ForeignKey(on_delete=False, to='app.OrderType'),
        ),
    ]
