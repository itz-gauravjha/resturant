# Generated by Django 5.0.6 on 2024-06-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_alter_category_options_alter_menuitem_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='product_desription',
            new_name='item_desription',
        ),
    ]
