# Generated by Django 3.0.7 on 2020-08-24 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200823_1336'),
        ('orders', '0008_auto_20200824_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statushistory',
            name='order',
        ),
        migrations.AddField(
            model_name='statushistory',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statushistory', to='customers.Customer'),
        ),
    ]
