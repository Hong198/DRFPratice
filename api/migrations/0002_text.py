# Generated by Django 5.1.4 on 2024-12-19 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=255, verbose_name='파일 이름')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_dt', models.DateTimeField(auto_now=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
        ),
    ]
