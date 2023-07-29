from decimal import Decimal
from typing import Optional
import uuid
import dataclasses


@dataclasses.dataclass
class Product:
    pk: Optional[uuid.UUID]
    title: str
    price: Decimal
