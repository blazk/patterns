#!/usr/bin/env python

# Visitor pattern example


# -----------------------
# A bunch of Visitables
# -----------------------

class Visitable(object):

    def accept(self, visitor):
        pass


class Necessity(Visitable):
    pass


class Milk(Necessity):

    name = 'milk'
    price = 0.99

    def accept(self, visitor):
        visitor.visit_milk(self)


class Bread(Necessity):

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


# ---------------------------------------------
# A couple of different Visitors.
#
# This implementation of Visitor pattern has a
# disadvantage over implementation in languages that
# support method overloading; in a language with
# method overloading we could define visit method
# with a signature
#    visit(Necessity necessity)
# This method would handle both Milk and Bread.
# In python we need to define explicit methods
# for handling Milk and Bread.
#
# The taxes2.py example shows alternative
# implementation which does not have this disadvantage.
# ---------------------------------------------


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
    Visitor with a state
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

tax_visitor = TaxVisitor()
milk.accept(tax_visitor)
bread.accept(tax_visitor)
tobacco.accept(tax_visitor)
liquor.accept(tax_visitor)

total = TotalPriceVisitor()
milk.accept(total)
bread.accept(total)
tobacco.accept(total)
liquor.accept(total)
total.show()

