# Generated by Django 3.0.4 on 2020-04-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king', '0002_remove_king_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='king',
            name='picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
