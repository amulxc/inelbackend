from django.db import migrations

def migrate_type_to_types(apps, schema_editor):
    Product = apps.get_model('base', 'Product')
    for product in Product.objects.all():
        if hasattr(product, 'type_id') and product.type_id:
            product.types.add(product.type_id)
            product.save()

def reverse_migrate(apps, schema_editor):
    Product = apps.get_model('base', 'Product')
    for product in Product.objects.all():
        types = product.types.all()
        if types.exists():
            product.type_id = types.first().id
            product.save()

class Migration(migrations.Migration):
    dependencies = [
        ('base', '0011_product_specifications_image'),
    ]

    operations = [
        migrations.RunPython(migrate_type_to_types, reverse_migrate),
    ]