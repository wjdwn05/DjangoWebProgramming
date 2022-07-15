# Generated by Django 4.0.5 on 2022-06-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='슬러그')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='요약')),
                ('content', models.TextField(verbose_name='본문')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={
                'verbose_name': '포스트',
                'verbose_name_plural': '포스트',
                'ordering': ('-modify_dt',),
            },
        ),
    ]
