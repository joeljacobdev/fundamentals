import random
import uuid
from http import HTTPStatus
from typing import Optional, List
import logging

logger = logging.getLogger('shopify')


class ShopifyMarketplaceClient:
    def __init__(self, account_id):
        self.account_id = account_id

    def get_products(self) -> List[dict]:
        # make some api call to amazon marketplace using the merchant id
        logger.info(f'Getting product data for account id={self.account_id}')
        return [
            {'id': uuid.uuid4(), 'title': 'iPhone 14 Pro', 'cost': '89999.99', 'image': ''},
            {'id': uuid.uuid4(), 'title': 'iPhone 12 Mini', 'cost': '67998.00', 'image': ''}
        ]

    def add_product(self, product: dict) -> Optional[uuid.UUID]:
        """
        :param product:
        :return: uuid of the created product
        """
        # api call to add product
        logger.info(f'Add product={product} to account id={self.account_id}')
        return random.choice([uuid.uuid4(), None])

    def remove_product(self, product_id) -> HTTPStatus:
        """
        :param product_id:
        :return: status code of api. It is removed successfully when status is 200.
        """
        # api call to remove product
        logger.info(f'Removing product id={product_id} of account id={self.account_id}')
        res = {'status': random.choice(
            [HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.BAD_GATEWAY, HTTPStatus.BAD_REQUEST, HTTPStatus.NOT_FOUND]
        )}
        return res['status']
