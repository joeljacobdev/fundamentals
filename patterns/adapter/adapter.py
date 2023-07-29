import abc
import uuid
from decimal import Decimal
from http import HTTPStatus
from typing import List

from amazon_marketplace import Client as AmazonMarketplaceClient
from models import Product
from shopify import Client as ShopifyClient


class BaseMarketplaceAdapter(abc.ABC):

    def __init__(self, account_id):
        self.client = NotImplemented

    @abc.abstractmethod
    def get_products(self) -> List[Product]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_product(self, product: Product) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_product(self, product: Product) -> bool:
        raise NotImplementedError


class ShopifyAdapter(BaseMarketplaceAdapter):

    def __init__(self, account_id):
        super().__init__(account_id)
        self.client = ShopifyClient(account_id)

    def get_products(self) -> List[Product]:
        response = self.client.get_products()
        products = []
        for product in response:
            products.append(Product(pk=product['id'], title=product['title'], price=Decimal(product['cost'])))
        return products

    def add_product(self, product: Product) -> bool:
        response = self.client.add_product({'title': product.title, 'cost': str(product.price)})
        return response is not None

    def remove_product(self, product: Product) -> bool:
        response = self.client.remove_product(product.pk)
        return response == HTTPStatus.OK


class AmazonAdapter(BaseMarketplaceAdapter):

    def __init__(self, account_id):
        super().__init__(account_id)
        self.client = AmazonMarketplaceClient(merchant_id=account_id)

    def get_products(self) -> List[Product]:
        response = self.client.get_products()
        products = []
        for product in response:
            products.append(Product(pk=product['id'], title=product['name'], price=Decimal(product['price'])))
        return products

    def add_product(self, product: Product) -> bool:
        response = self.client.add_product({'name': product.title, 'price': float(product.price)})
        return response.get('id') is not None

    def remove_product(self, product: Product) -> bool:
        return self.client.remove_product({'id': product.pk, 'name': product.title, 'price': float(product.price)})


"""
Adapter is used when we need to have common interface for third party libraries/packages in our code.
It is different from interface as we can't modify third party code, and interface is used for our code.
"""
account_id = 'ACADAX#D'
product = Product(pk=None, title='Apple Macbook Air 15', price=Decimal(199989.00))
remove_product = Product(pk=uuid.uuid4(), title='Apple Macbook Air 15', price=Decimal(199989.00))
market_place = ShopifyAdapter(account_id)
print(market_place.get_products())
print(market_place.add_product(product))
print(market_place.remove_product(remove_product))
market_place = AmazonAdapter(account_id)
print(market_place.get_products())
print(market_place.add_product(product))
print(market_place.remove_product(remove_product))
