# Generated by Django 4.0.5 on 2022-10-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_customer_pswd_alter_customer_email_alter_mobile_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]