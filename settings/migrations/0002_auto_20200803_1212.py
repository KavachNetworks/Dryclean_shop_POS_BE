# Generated by Django 3.0.7 on 2020-08-03 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='enterprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority', to='enterprise.Enterprise'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='enterprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='enterprise.Enterprise'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='enterprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='enterprise.Enterprise'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority', to='settings.Priority'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='settings.ProductType'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='settings.ServiceType'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='enterprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='enterprise.Enterprise'),
        ),
    ]
