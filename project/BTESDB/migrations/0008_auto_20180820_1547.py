# Generated by Django 2.1 on 2018-08-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTESDB', '0007_auto_20180820_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damage_state_test',
            name='id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
