# Generated by Django 2.2.3 on 2019-07-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_personal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name': 'personal', 'verbose_name_plural': 'personal'},
        ),
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]