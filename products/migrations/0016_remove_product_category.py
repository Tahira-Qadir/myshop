# Generated by Django 5.0.3 on 2024-03-10 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_category_delete_shirt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]