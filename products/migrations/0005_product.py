# Generated by Django 5.0.3 on 2024-03-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_shirt_is_bestselller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
