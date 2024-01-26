# Generated by Django 5.0.1 on 2024-01-21 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_author_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.comment'),
        ),
    ]
