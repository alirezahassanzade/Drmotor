# Generated by Django 2.1.5 on 2019-03-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190227_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
