# Generated by Django 4.2.10 on 2024-02-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="invite_code",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=254,
                null=True,
                verbose_name="Инвайт-код",
            ),
        ),
    ]
