# Generated by Django 5.1.2 on 2024-11-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zoo", "0002_animal_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
