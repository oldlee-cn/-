# Generated by Django 2.2 on 2019-04-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FromTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='姓名')),
                ('email', models.EmailField(max_length=20, verbose_name='邮箱')),
                ('adsress', models.CharField(max_length=100, verbose_name='地址')),
                ('message', models.CharField(max_length=500, verbose_name='信息')),
            ],
        ),
    ]
