# Generated by Django 4.0.3 on 2022-07-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_lead_date_added_lead_description_lead_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]