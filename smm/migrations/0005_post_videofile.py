# Generated by Django 3.2.7 on 2021-09-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smm', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(default='default.mp4', null=True, upload_to='videos/', verbose_name=''),
        ),
    ]