# Generated by Django 3.0.4 on 2020-03-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_remove_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]