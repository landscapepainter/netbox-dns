# Generated by Django 4.0.4 on 2022-04-26 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_dns', '0010_update_soa_records'),
        ('netbox_dns', '0011_add_view_model'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='unique_pointer_for_address',
        ),
    ]
