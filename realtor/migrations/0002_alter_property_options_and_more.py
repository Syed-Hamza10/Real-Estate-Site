# Generated by Django 4.2.3 on 2023-09-05 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("realtor", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="property",
            options={"verbose_name_plural": "Properties"},
        ),
        migrations.AlterModelOptions(
            name="propertycategory",
            options={"verbose_name_plural": "Property Categories"},
        ),
        migrations.AlterModelOptions(
            name="propertyfeature",
            options={"verbose_name_plural": "Property Features"},
        ),
    ]