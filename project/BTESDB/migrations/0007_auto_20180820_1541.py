# Generated by Django 2.1 on 2018-08-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTESDB', '0006_auto_20180816_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage_state_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DB_part', models.CharField(default='', max_length=14, verbose_name='易损件')),
                ('damage_id', models.SmallIntegerField(verbose_name='损伤编号')),
                ('damage_state', models.CharField(blank=True, max_length=45, verbose_name='损伤状态')),
                ('damage_description', models.CharField(max_length=300, verbose_name='损伤状态描述')),
                ('median', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='中位值')),
                ('variance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='方差')),
                ('lost_parameter', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='损失参数')),
                ('rehabilitation_coeffcient', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='修复系数')),
                ('min_rehab_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='最小工程量折减数量(修复费用)')),
                ('min_lost_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='工程量折减系数(修复费用)')),
                ('max_rehab_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='最大工程量折减数量(修复费用)')),
                ('max_lost_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='工程量折减系数(修复费用)')),
                ('cov_cost', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='费用COV')),
                ('repair_people_day', models.IntegerField(blank=True, verbose_name='修复时间(人*天)')),
                ('min_rehab_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='最小工程量折减数量(修复时间)')),
                ('min_lost_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='工程量折减系数(修复时间)')),
                ('max_rehab_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='最大工程量折减数量(修复时间)')),
                ('max_lost_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='工程量折减系数(修复时间)')),
                ('cov_time', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='时间COV')),
            ],
            options={
                'verbose_name': '易损件损伤临时',
                'verbose_name_plural': '易损件损伤详情临时',
            },
        ),
        migrations.AlterField(
            model_name='damage_state_detail',
            name='damage_state',
            field=models.CharField(blank=True, max_length=45, verbose_name='损伤状态'),
        ),
        migrations.AlterUniqueTogether(
            name='damage_state_test',
            unique_together={('DB_part', 'damage_id')},
        ),
    ]
