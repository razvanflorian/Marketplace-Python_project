# Generated by Django 5.1 on 2024-08-24 20:38

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
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight_grams', models.IntegerField()),
                ('available_quantity', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_imageS')),
            ],
        ),
    ]
