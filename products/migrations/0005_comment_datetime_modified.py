# Generated by Django 4.0.2 on 2022-09-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_satisfaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
