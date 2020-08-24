# Generated by Django 3.0.7 on 2020-08-24 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200821_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statushistory',
            name='customer',
        ),
        migrations.AddField(
            model_name='statushistory',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statushistory', to='orders.Order'),
        ),
    ]
