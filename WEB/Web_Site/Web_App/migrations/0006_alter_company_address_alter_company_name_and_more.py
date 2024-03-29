from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0005_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='(Скидка в процентах)', max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['user', 'order_date'], name='Web_App_ord_user_id_5c1683_idx'),
        ),
    ]
