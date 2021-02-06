# Generated by Django 3.1.6 on 2021-02-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issue_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receive_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='reorder_level',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]