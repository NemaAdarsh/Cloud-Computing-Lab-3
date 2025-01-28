import json
from products import Product, get_product
from cart import dao


class Cart:
    # def _init_(self, id: int, username: str, contents: list[Product], cost: float):
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    # def load(data):
    @staticmethod
    def load(data: dict) -> "Cart":
        return Cart(
            id=data["id"],
            username=data["username"],
            contents=data["contents"],
            cost=data["cost"],
        )


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        # contents = eval(cart_detail["contents"])  
        try:
            contents = json.loads(cart_detail["contents"])
        except json.JSONDecodeError:
            continue

        # for content in contents:
        #     items.append(content)
        items.extend(contents)

    # i2 = []
    # for i in items:
    #     temp_product = products.get_product(i)
    #     i2.append(temp_product)
    return [get_product(product_id) for product_id in items]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
