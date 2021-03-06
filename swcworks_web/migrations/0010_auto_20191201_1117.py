# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-01 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swcworks_web', '0009_auto_20191201_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swtable13',
            name='totalnum',
            field=models.IntegerField(null=True, verbose_name='2019年全省范围内志愿者培训总人数'),
        ),
        migrations.AlterField(
            model_name='swtable15',
            name='nzyfwss',
            field=models.IntegerField(null=True, verbose_name='其中：2019年志愿服务时数（小时）'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='czzjtr',
            field=models.IntegerField(null=True, verbose_name='2019年财政资金投入'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='fcjtr',
            field=models.IntegerField(null=True, verbose_name='2019年福彩金投入'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='cpgyj',
            field=models.IntegerField(null=True, verbose_name='2019年彩票公益金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='czxzj',
            field=models.IntegerField(null=True, verbose_name='2019年财政性资金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='qtzj',
            field=models.IntegerField(null=True, verbose_name='2019年其他资金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='zjtr_total',
            field=models.IntegerField(null=True, verbose_name='2019年总计投入'),
        ),
        migrations.AlterField(
            model_name='swtable5',
            name='year_tag',
            field=models.CharField(choices=[('2019', '2019年社会工作培训情况')], max_length=8, null=True, verbose_name='统计年份'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='zjtrzl',
            field=models.IntegerField(null=True, verbose_name='2019年资金投入总量（万元）'),
        ),
    ]
