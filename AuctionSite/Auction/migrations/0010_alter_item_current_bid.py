# Generated by Django 4.0 on 2022-11-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0009_rename_bids_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='current_bid',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]