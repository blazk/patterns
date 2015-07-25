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

    def accept(self, visitor):
        visitor.visit_necessity(self)


class Milk(Necessity):

    name = 'milk'
    price = 0.99


class Bread(Necessity):

    name = 'bread'
    price = 0.6


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
# A couple of different Visitors
# -------------------------------


class Visitor(object):

    def visit_necessity(self, necessity):
        pass

    def visit_tobacco(self, tobacco):
        pass

    def visit_liquor(self, liquor):
        pass



class NetVisitor(Visitor):

    def visit_necessity(self, necessity):
        print necessity.name, "price:", necessity.price

    def visit_tobacco(self, tobacco):
        print tobacco.name, "price:", tobacco.price

    def visit_liquor(self, item):
        print liquor.name, "price:", liquor.price



class TaxVisitor(Visitor):

    def visit_necessity(self, necessity):
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

