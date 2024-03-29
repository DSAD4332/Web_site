# Generated by Django 5.0 on 2023-12-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0006_alter_company_address_alter_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin'), ('company', 'Company')], default='customer', max_length=10),
        ),
    ]
