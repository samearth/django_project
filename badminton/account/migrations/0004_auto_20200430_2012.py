# Generated by Django 3.0.2 on 2020-04-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='id',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
