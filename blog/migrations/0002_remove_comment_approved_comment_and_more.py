# Generated by Django 4.2.3 on 2023-08-10 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="approved_comment",
        ),
        migrations.RemoveField(
            model_name="post",
            name="categories",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
