# Generated by Django 3.0.2 on 2020-05-02 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200502_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints_posted',
            name='Downvote',
        ),
        migrations.RemoveField(
            model_name='complaints_posted',
            name='Upvote',
        ),
    ]