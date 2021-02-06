# Generated by Django 3.1.6 on 2021-02-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_auto_20210205_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
