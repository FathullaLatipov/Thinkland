from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })


    class Index:
        name = 'products'

    class Django:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'unit',
            'price',
            'main_image',
        ]