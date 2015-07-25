#!/usr/bin/env python

# Visitor pattern.
# Original Java example:
# https://www.youtube.com/watch?v=pL4mOUDi54o


# ------------------
# Visitables
# ------------------


class Visitable(object):

    def accept(self, visitor):
        pass


class Necessity(Visitable):

    price = 4.5

    def accept(self, visitor):
        visitor.visit_necessity(self)


class Tobacco(Visitable):

    price = 9.85

    def accept(self, visitor):
        visitor.visit_tobacco(self)


class Liquor(Visitable):

    price = 17.0

    def accept(self, visitor):
        visitor.visit_liquor(self)



# -------------------
# Visitor
# -------------------


class Visitor(object):

    def visit_necessity(self, necessity):
        pass

    def visit_tobacco(self, necessity):
        pass

    def visit_liquor(self, necessity):
        pass



class NetVisitor(Visitor):

    def visit_necessity(self, necessity):
        print "Necessity price:", necessity.price

    def visit_tobacco(self, tobacco):
        print "Tobacco price:", tobacco.price

    def visit_liquor(self, liquor):
        print "Liquor price:", liquor.price



class TaxVisitor(Visitor):

    def visit_necessity(self, necessity):
        x = necessity.price
        print "Necessity price with tax:", x

    def visit_tobacco(self, tobacco):
        x = tobacco.price
        print "Tobacco price with tax:", x + x * 0.3

    def visit_liquor(self, liquor):
        x = liquor.price
        print "Liquor price with tax:", x + x * 0.2




necessity = Necessity()
tobacco = Tobacco()
liquor = Liquor()

net_visitor = NetVisitor()
necessity.accept(net_visitor)
tobacco.accept(net_visitor)
liquor.accept(net_visitor)

tax_visitor = TaxVisitor()
necessity.accept(tax_visitor)
tobacco.accept(tax_visitor)
liquor.accept(tax_visitor)

