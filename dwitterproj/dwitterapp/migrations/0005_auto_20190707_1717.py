# Generated by Django 2.0.5 on 2019-07-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitterapp', '0004_auto_20190706_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test2',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='test2',
            name='username',
            field=models.TextField(max_length=100),
        ),
    ]
