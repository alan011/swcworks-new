# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swcworks_web', '0006_auto_20181216_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swtable1',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable1',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省/直辖市'),
        ),
        migrations.AlterField(
            model_name='swtable10',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable10',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省/直辖市'),
        ),
        migrations.AlterField(
            model_name='swtable11',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable11',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable12',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable12',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable13',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable13',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable14',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable14',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable15',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable15',
            name='nzyfwss',
            field=models.IntegerField(null=True, verbose_name='其中：2018年志愿服务时数（小时）'),
        ),
        migrations.AlterField(
            model_name='swtable15',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='czzjtr',
            field=models.IntegerField(null=True, verbose_name='2018年财政资金投入'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='fcjtr',
            field=models.IntegerField(null=True, verbose_name='2018年福彩金投入'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable16',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='cpgyj',
            field=models.IntegerField(null=True, verbose_name='2018年彩票公益金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='czxzj',
            field=models.IntegerField(null=True, verbose_name='2018年财政性资金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='level',
            field=models.IntegerField(choices=[(1, '省级层面'), (2, '全省总计投入资金')], null=True, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='qtzj',
            field=models.IntegerField(null=True, verbose_name='2018年其他资金（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='qtzj_comments',
            field=models.TextField(null=True, verbose_name='其他资金备注'),
        ),
        migrations.AlterField(
            model_name='swtable17',
            name='zjtr_total',
            field=models.IntegerField(null=True, verbose_name='2018年总计投入'),
        ),
        migrations.AlterField(
            model_name='swtable2',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（区、市）'),
        ),
        migrations.AlterField(
            model_name='swtable3',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable3',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（区、市）'),
        ),
        migrations.AlterField(
            model_name='swtable4',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable4',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable4',
            name='weishengjisheng',
            field=models.IntegerField(default=0, verbose_name='卫健'),
        ),
        migrations.AlterField(
            model_name='swtable5',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable5',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable5',
            name='year_tag',
            field=models.CharField(choices=[('2018', '2018年社会工作培训情况')], max_length=8, null=True, verbose_name='统计年份'),
        ),
        migrations.AlterField(
            model_name='swtable6',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable6',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable7',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable7',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='comments',
            field=models.TextField(default='', verbose_name='备注其他资金来源'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='description',
            field=models.TextField(default='', verbose_name='“民政部本级彩票金社会工作和志愿服务项目”资金使用方式及用途（开展项目、活动名称及简介）'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
        migrations.AlterField(
            model_name='swtable8',
            name='zjtrzl',
            field=models.IntegerField(null=True, verbose_name='2018年资金投入总量（万元）'),
        ),
        migrations.AlterField(
            model_name='swtable9',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='swtable9',
            name='province',
            field=models.CharField(choices=[('Beijing', '1、北京市'), ('Tianjin', '2、天津市'), ('Shanghai', '3、上海市'), ('Chongqing', '4、重庆市'), ('Heilongjiang', '5、黑龙江省'), ('Jilin', '6、吉林省'), ('Liaoning', '7、辽宁省'), ('Hebei', '8、河北省'), ('Neimenggu', '9、内蒙古自治区'), ('Shanxi', '10、山西省'), ('Shandong', '11、山东省'), ('Henan', '12、河南省'), ('Anhui', '13、安徽省'), ('Jiangsu', '14、江苏省'), ('Zhejiang', '15、浙江省'), ('Fujian', '16、福建省'), ('Jiangxi', '17、江西省'), ('Guangdong', '18、广东省'), ('Hubei', '19、湖北省'), ('Hunan', '20、湖南省'), ('Guangxi', '21、广西壮族自治区'), ('Hainan', '22、海南省'), ('Yunnan', '23、云南省'), ('Guizhou', '24、贵州省'), ('Sichuan', '25、四川省'), ('ShanVxi', '26、陕西省'), ('Ningxia', '27、宁夏回族自治区'), ('Gansu', '28、甘肃省'), ('Xizhang', '29、西藏自治区'), ('Qinghai', '30、青海省'), ('Xinjiang', '31、新疆维吾尔族自治区'), ('Xianggang', '32、香港特别行政区'), ('Aomen', '33、澳门特别行政区'), ('Taiwan', '34、台湾省'), ('XinjiangSCJSBT', '35、新疆生产建设兵团')], max_length=32, null=True, verbose_name='省（市、区）'),
        ),
    ]
