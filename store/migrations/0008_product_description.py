# Generated by Django 4.1.7 on 2023-05-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_alter_customer_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
