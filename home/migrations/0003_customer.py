# Generated by Django 3.2.4 on 2021-06-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('join_data', models.DateField()),
            ],
        ),
    ]