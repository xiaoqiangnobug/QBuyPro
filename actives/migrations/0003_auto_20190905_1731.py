# Generated by Django 2.0.1 on 2019-09-05 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actives', '0002_auto_20190905_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activegoodsmodel',
            options={'verbose_name': '活动信息', 'verbose_name_plural': '活动信息'},
        ),
        migrations.AlterModelOptions(
            name='activemodel',
            options={'verbose_name': '活动', 'verbose_name_plural': '活动'},
        ),
    ]
