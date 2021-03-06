# Generated by Django 3.0.7 on 2020-08-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200820_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='rate',
        ),
        migrations.AddField(
            model_name='order',
            name='advance_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
