# Generated by Django 4.0 on 2022-02-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='topics/images/'),
        ),
    ]
