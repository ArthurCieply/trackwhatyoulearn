# Generated by Django 4.0.2 on 2022-02-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_alter_topic_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='image',
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
    ]
