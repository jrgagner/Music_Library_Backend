# Generated by Django

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_song_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]