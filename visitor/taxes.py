#!/usr/bin/env python

# Visitor pattern example

# -----------------------
# Visitables
# -----------------------

class Visitable(object):

    def accept(self, visitor):
        pass


class Milk(Visitable):

    name = 'milk'
    price = 0.99

    def accept(self, visitor):
        visitor.visit_milk(self)


class Bread(Visitable):

    name = 'bread'
    price = 0.6

    def accept(self, visitor):
        visitor.visit_bread(self)


class Tobacco(Visitable):

    name = 'tobacco'
    price = 10.0

    def accept(self, visitor):
        visitor.visit_tobacco(self)


class Liquor(Visitable):

    name = 'liquor'
    price = 20.0

    def accept(self, visitor):
        visitor.visit_liquor(self)


# -------------------------------
# A couple of different Visitors.
# -------------------------------


class Visitor(object):

    def visit_milk(self, milk):
        pass

    def visit_bread(self, bread):
        pass

    def visit_tobacco(self, tobacco):
        pass

    def visit_liquor(self, liquor):
        pass


class TaxVisitor(Visitor):

    """
    calculates price after tax for each item type
    """

    def visit_milk(self, milk):
        name = milk.name
        price = milk.price
        print name, "price with tax:", price

    def visit_bread(self, bread):
        name = bread.name
        price = bread.price
        print name, "price with tax:", price

    def visit_tobacco(self, tobacco):
        name = tobacco.name
        price = tobacco.price
        print name, "price with tax:", price + price * 0.3

    def visit_liquor(self, liquor):
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

    def visit_milk(self, milk):
        self._total += milk.price

    def visit_bread(self, bread):
        self._total += bread.price

    def visit_tobacco(self, tobacco):
        self._total += tobacco.price

    def visit_liquor(self, liquor):
        self._total += liquor.price

    def show(self):
        print "Total price (without tax):", self._total


milk = Milk()
bread = Bread()
tobacco = Tobacco()
liquor = Liquor()

tax = TaxVisitor()
milk.accept(tax)
bread.accept(tax)
tobacco.accept(tax)
liquor.accept(tax)

total = TotalPriceVisitor()
milk.accept(total)
bread.accept(total)
tobacco.accept(total)
liquor.accept(total)
total.show()
