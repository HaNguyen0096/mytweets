# Generated by Django 2.2 on 2020-08-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20200805_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
