# Generated by Django 2.0.6 on 2018-06-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderform', '0003_auto_20180609_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='c1T100_slice',
            field=models.CharField(default='不切', max_length=10, verbose_name='鮮奶吐司-切片'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T100_thickless',
            field=models.CharField(default='', max_length=10, verbose_name='鮮奶吐司-厚度'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T120_slice',
            field=models.CharField(default='不切', max_length=10, verbose_name='葡萄乾吐司-切片'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T120_thickless',
            field=models.CharField(default='', max_length=10, verbose_name='葡萄乾吐司-厚度'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T130_slice',
            field=models.CharField(default='不切', max_length=10, verbose_name='蔓越莓吐司-切片'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T130_thickless',
            field=models.CharField(default='', max_length=10, verbose_name='蔓越莓吐司-厚度'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T140_slice',
            field=models.CharField(default='不切', max_length=10, verbose_name='核桃吐司-切片'),
        ),
        migrations.AddField(
            model_name='order',
            name='c1T140_thickless',
            field=models.CharField(default='', max_length=10, verbose_name='核桃吐司-厚度'),
        ),
        migrations.AddField(
            model_name='order',
            name='c2M50_slice',
            field=models.CharField(default='不切', max_length=10, verbose_name='酵母鬆餅-切片'),
        ),
        migrations.AddField(
            model_name='order',
            name='c2M50_thickless',
            field=models.CharField(default='', max_length=10, verbose_name='酵母鬆餅-厚度'),
        ),
        migrations.AlterField(
            model_name='order',
            name='c1T100',
            field=models.IntegerField(verbose_name='鮮奶吐司'),
        ),
        migrations.AlterField(
            model_name='order',
            name='c1T120',
            field=models.IntegerField(verbose_name='葡萄乾吐司'),
        ),
        migrations.AlterField(
            model_name='order',
            name='c1T130',
            field=models.IntegerField(verbose_name='蔓越莓吐司'),
        ),
        migrations.AlterField(
            model_name='order',
            name='c1T140',
            field=models.IntegerField(verbose_name='核桃吐司'),
        ),
        migrations.AlterField(
            model_name='order',
            name='c2M50',
            field=models.IntegerField(verbose_name='酵母鬆餅'),
        ),
    ]
