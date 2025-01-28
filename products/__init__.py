from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    # Unoptimized code:
    # products = dao.list_products()
    # result = []
    # for product in products:
    #     result.append(Product.load(product))
    
    # Optimized code:
    products = dao.list_products()
    return [Product.load(product) for product in products]  # List comprehension is more efficient and concise

    # return result  # No need for this manual loop with list comprehension.


def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
