# Generated by Django 5.0.2 on 2024-05-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_description', models.TextField()),
            ],
        ),
    ]
    

