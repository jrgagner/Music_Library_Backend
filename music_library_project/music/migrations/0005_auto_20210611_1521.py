# Generated by Django

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20221211_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]