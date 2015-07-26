#!/usr/bin/env python

# Visitor pattern.
# Adapted from original Java example
# https://www.youtube.com/watch?v=pL4mOUDi54o


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



class NetVisitor(Visitor):

    def visit_milk(self, milk):
        print milk.name, "price:", milk.price

    def visit_bread(self, bread):
        print bread.name, "price:", bread.price

    def visit_tobacco(self, tobacco):
        print tobacco.name, "price:", tobacco.price

    def visit_liquor(self, item):
        print liquor.name, "price:", liquor.price



class TaxVisitor(Visitor):

    def visit_milk(self, necessity):
        name = necessity.name
        price = necessity.price
        print name, "price with tax:", price

    def visit_tobacco(self, tobacco):
        name = tobacco.name
        price = tobacco.price
        print name, "price with tax:", price + price * 0.3

    def visit_liquor(self, liquor):
        name = liquor.name
        price = liquor.price
        print name, "price with tax:", price + price * 0.2




milk = Milk()
bread = Bread()
tobacco = Tobacco()
liquor = Liquor()

net_visitor = NetVisitor()
milk.accept(net_visitor)
bread.accept(net_visitor)
tobacco.accept(net_visitor)
liquor.accept(net_visitor)

tax_visitor = TaxVisitor()
milk.accept(tax_visitor)
bread.accept(tax_visitor)
tobacco.accept(tax_visitor)
liquor.accept(tax_visitor)

