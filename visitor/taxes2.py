#!/usr/bin/env python

# Visitor pattern example 2

# -----------------------
# Visitables
# -----------------------

class StockItem(object):
    pass


class Necessity(StockItem):
    pass


class Milk(Necessity):
    name = 'milk'
    price = 0.99


class Bread(Necessity):
    name = 'bread'
    price = 0.6


class Tobacco(StockItem):
    name = 'tobacco'
    price = 10.0


class Liquor(StockItem):
    name = 'liquor'
    price = 20.0


# -------------------------------
# A couple of different Visitors.
# -------------------------------


class Visitor(object):

    def visit(self, visitable):
        visitable_class_hierarchy = [t.__name__ for t in type(visitable).mro()]
        for visitable_class_name in visitable_class_hierarchy:
            handler_name = 'visit_' + visitable_class_name
            handler = getattr(self, handler_name, None)
            if handler is None:
                continue
            return handler(visitable)
        return self.fallback(visitable)

    def fallback(self, visitable):
        raise RuntimeError('{} of type {} is not supported'.format(
                repr(visitable), type(visitable)))



class TaxVisitor(Visitor):

    """
    calculates price after tax for each item type
    """

    def visit_Necessity(self, necessity):
        name = necessity.name
        price = necessity.price
        print name, "price with tax:", price

    def visit_Tobacco(self, tobacco):
        name = tobacco.name
        price = tobacco.price
        print name, "price with tax:", price + price * 0.3

    def visit_Liquor(self, liquor):
        name = liquor.name
        price = liquor.price
        print name, "price with tax:", price + price * 0.2


class TotalPriceVisitor(Visitor):

    """
    Calculates total price.
    An example of a Visitor with state.
    """

    def __init__(self):
        self._total = 0.0

    def visit_StockItem(self, item):
        self._total += item.price

    def show(self):
        print "Total price (without tax):", self._total



milk = Milk()
bread = Bread()
tobacco = Tobacco()
liquor = Liquor()

tax = TaxVisitor()
tax.visit(milk)
tax.visit(bread)
tax.visit(tobacco)
tax.visit(liquor)

total = TotalPriceVisitor()
total.visit(milk)
total.visit(bread)
total.visit(tobacco)
total.visit(liquor)
total.show()

## OUTPUT:
# milk price with tax: 0.99
# bread price with tax: 0.6
# tobacco price with tax: 13.0
# liquor price with tax: 24.0
# Total price (without tax): 31.59

