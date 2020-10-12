# Generated by Django 3.1.1 on 2020-10-12 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='블로그 글의 분류를 입력하세요.(ex:일상)', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(help_text='글의 분류를 설정하세요.', to='blog.Category'),
        ),
    ]
