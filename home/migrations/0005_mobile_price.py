# Generated by Django 4.0.5 on 2022-10-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tag_mobile_date_mobile_image_mobile_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='price',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
