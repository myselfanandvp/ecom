# Generated by Django 5.2.1 on 2025-05-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images/')),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
