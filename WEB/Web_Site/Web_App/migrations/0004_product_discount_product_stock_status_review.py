# Generated by Django 4.2.7 on 2023-12-12 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0003_alter_company_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Скидка в процентах', max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_status',
            field=models.CharField(choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], default='in_stock', max_length=15),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Web_App.company')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Web_App.product')),
            ],
        ),
    ]
