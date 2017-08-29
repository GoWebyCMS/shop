from .cart import Cart


def cart(request):
    """ Makes cart information global """

    return {'cart': Cart(request)}