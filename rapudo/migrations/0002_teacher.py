# Generated by Django 5.0.2 on 2024-05-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapudo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_description', models.TextField()),
            ],
        ),
    ]

     
