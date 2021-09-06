# Generated by Django 2.2 on 2021-09-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='valuecomodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='valueco_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'VALUECO',
                'db_table': 'valueco',
            },
        ),
    ]
