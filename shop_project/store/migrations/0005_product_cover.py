# Generated by Django 4.1.7 on 2023-03-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
