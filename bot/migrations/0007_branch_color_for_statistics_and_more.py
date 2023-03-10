# Generated by Django 4.0.6 on 2022-09-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_rename_telegram_group_name1_branch_telegraph_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='color_for_statistics',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='data_for_statistics',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='total_for_statistics',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='branch_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order_items',
            name='branch_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order_items',
            name='date_ordered',
            field=models.DateField(auto_now_add=True),
        ),
    ]
