# Generated by Django 4.0.3 on 2022-07-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='uploades/'),
        ),
    ]
