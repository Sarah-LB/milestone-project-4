# Generated by Django 3.2 on 2022-12-02 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
