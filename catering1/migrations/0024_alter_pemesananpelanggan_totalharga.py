# Generated by Django 5.1.1 on 2024-11-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0023_alter_pelanggan_password_alter_pelanggan_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemesananpelanggan',
            name='totalHarga',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Total Harga'),
        ),
    ]