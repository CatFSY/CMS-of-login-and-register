# Generated by Django 4.2.6 on 2023-10-16 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_article_created_at_alter_article_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]