# Generated by Django 4.0 on 2022-10-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0006_alter_item_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
