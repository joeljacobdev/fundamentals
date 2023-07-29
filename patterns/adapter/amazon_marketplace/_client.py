import random
import uuid
from typing import List
from http import HTTPStatus
import logging

logger = logging.getLogger('amazon_marketplace')


class AmazonMarketplaceClientV4:
    """
    Client code for amazon market place, which is present in package - amazon-marketplace
    """

    def __init__(self, merchant_id):
        self.merchant_id = merchant_id

    def get_products(self) -> List[dict]:
        """
        :return: list of product dict
        """
        # make some api call to amazon marketplace using the merchant id
        logger.info(f'Getting products of merchant id={self.merchant_id}')
        return [
            {'id': uuid.uuid4(), 'name': 'iPhone 14 Pro', 'price': 89999.99, 'image': ''},
            {'id': uuid.uuid4(), 'name': 'iPhone 12 Mini', 'price': 67998.00, 'image': ''}
        ]

    def add_product(self, product: dict) -> dict:
        """
        :param product: dict
        :return: product dict having id of created product if success, otherwise return the whole input back
        """
        # api call to add product
        logger.info(f'Adding product={product} to merchant id={self.merchant_id}')
        res = {'id': random.choice([None, uuid.uuid4()])}
        if res.get('id'):
            product = {'id': res['id'], **product}
        return product

    def remove_product(self, product: dict) -> bool:
        """
        :param product: dict of product data having 'id'
        :return: true if product is removed successfully else false
        """
        # api call to remove product
        logger.info(f'Removing product={product} from merchant id={self.merchant_id}')
        res = {'status': random.choice(
            [HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.BAD_GATEWAY, HTTPStatus.BAD_REQUEST, HTTPStatus.NOT_FOUND]
        )}
        return res['status'] == HTTPStatus.OK
