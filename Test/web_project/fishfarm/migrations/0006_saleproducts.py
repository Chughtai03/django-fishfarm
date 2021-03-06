# Generated by Django 3.2.3 on 2021-06-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishfarm', '0005_auto_20210623_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='saleproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
