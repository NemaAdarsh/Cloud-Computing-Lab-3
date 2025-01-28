import cart
import products

def checkout(username: str) -> float:
    user_cart = cart.get_cart(username)
    if not user_cart:
        return 0
    total = sum(item.cost for item in user_cart)
    return total

def complete_checkout(username: str) -> None:
    user_cart = cart.get_cart(username)
    if not user_cart:
        raise ValueError("Cart is empty. Cannot complete checkout.")
    for item in user_cart:
        if item.qty < 1:
            raise ValueError(f"Invalid quantity for item {item.id}: {item.qty}. Must be at least 1.")
    for item in user_cart:
        products.update_qty(item.id, max(item.qty - 1, 0))
    cart.delete_cart(username)
