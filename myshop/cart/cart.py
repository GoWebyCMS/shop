from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """ Init the cart """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """ Adds a product to the cart or updates its quantity """

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """ updates the session cart """
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def remove(self, product):
        """ Removes a product from the cart """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        """ Iterates over the items in the cart and gets the products from the database """

        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

    def __len__(self):
        """ Counts all items in the cart and returns the total items in the cart"""

        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """ Calculates the total cost  for the items in the cart """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """ Clears the cart session """

        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True