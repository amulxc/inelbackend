# Generated by Django 4.1.9 on 2025-04-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_product_features_featureimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf_file',
            field=models.FileField(blank=True, help_text='Upload product PDF documentation', null=True, upload_to='static/products/pdfs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/products/images/'),
        ),
    ]
