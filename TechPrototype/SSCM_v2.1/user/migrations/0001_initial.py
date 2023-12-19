# Generated by Django 2.2.11 on 2023-12-17 13:54

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('m', '男'), ('f', '女')], default='m', max_length=10, verbose_name='性别')),
                ('number', models.CharField(max_length=30, primary_key=True, serialize=False, validators=[user.models.validate_length], verbose_name='教职工号')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=30, validators=[user.models.validate_pas_length], verbose_name='密码')),
                ('info', models.CharField(default='无', help_text='自我介绍，不超过250字', max_length=255, null=True, verbose_name='个人简介')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('m', '男'), ('f', '女')], default='m', max_length=10, verbose_name='性别')),
                ('grade', models.IntegerField(choices=[(1, 2017), (2, 2018), (3, 2019), (4, 2020), (5, 2021), (6, 2022), (7, 2023), (8, 2024)], default=1, verbose_name='入学年份')),
                ('number', models.CharField(max_length=30, primary_key=True, serialize=False, validators=[user.models.validate_stu_length], verbose_name='学号')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=30, validators=[user.models.validate_pas_length], verbose_name='密码')),
                ('info', models.CharField(default='无', help_text='自我介绍，不超过250字', max_length=255, null=True, verbose_name='个人简介')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('m', '男'), ('f', '女')], default='m', max_length=10, verbose_name='性别')),
                ('number', models.CharField(max_length=30, primary_key=True, serialize=False, validators=[user.models.validate_length], verbose_name='教职工号')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=30, validators=[user.models.validate_pas_length], verbose_name='密码')),
                ('info', models.CharField(default='无', help_text='自我介绍，不超过250字', max_length=255, null=True, verbose_name='个人简介')),
            ],
        ),
    ]