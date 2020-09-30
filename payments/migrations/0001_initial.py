# Generated by Django 3.0.7 on 2020-09-30 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0004_delete_payments'),
        ('orders', '0012_statushistory_workshop'),
        ('settings', '0005_auto_20200820_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enterprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='enterprise.Enterprise')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='orders.Order')),
                ('payment_mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='settings.PaymentModes')),
            ],
        ),
    ]
