from django.core.management import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Red Panda'},
            {'name': 'Qinling Pandas'},
            {'name': 'Giant Panda'},
            {'name': 'Kung Fu Panda'},
        ]

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Po', 'description': 'Kung Fu Panda', 'category': 'Kung Fu Panda', 'purchase_price': '55'},

            {'name': 'Red',
             'description': 'The red panda is slightly larger than a domestic cat with a bear-like body and thick russet fur.',
             'category': 'Red Panda', 'purchase_price': '155', },

            {'name': 'Panda',
             'description': 'The panda, with its distinctive black and white coat, '
                            'is adored by the world and considered a national treasure in China.',
             'category': 'Giant Panda', 'purchase_price': '125'},

            {'name': 'Qinling Panda',
             'description': ' Qinling panda (Ailuropoda melanoleuca qinlingensis ) is a subspecies of '
                            'the giant panda, discovered in the 1960s but not recognized as a subspecies until 2005.',
             'category': 'Qinling Pandas', 'purchase_price': '96'}

        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_for_create)
