# Generated by Django 5.0.4 on 2024-05-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0017_remove_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
