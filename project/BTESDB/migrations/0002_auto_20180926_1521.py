# Generated by Django 2.1 on 2018-09-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTESDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor_info',
            name='influence_coefficient',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='楼层影响系数'),
        ),
    ]