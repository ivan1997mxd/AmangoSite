# Generated by Django 2.2 on 2019-05-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190526_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品', 'verbose_name_plural': '产品方案'},
        ),
        migrations.AlterField(
            model_name='product',
            name='case',
            field=models.TextField(verbose_name='产品案例'),
        ),
        migrations.AlterField(
            model_name='product',
            name='customer',
            field=models.CharField(max_length=15, verbose_name='目标客户'),
        ),
        migrations.AlterField(
            model_name='product',
            name='function',
            field=models.TextField(verbose_name='产品功能'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=15, verbose_name='产品名称'),
        ),
    ]
