from strategy_pattern.Duck import Duck
from strategy_pattern.jet_flying import JetFlying
from strategy_pattern.simple_flying import SimpleFlying

from strategy_pattern.loud_quack import LoudQuack
from strategy_pattern.simple_quack import SimpleQuack

simple_flying_obj = SimpleFlying()
simple_quacking_obj = SimpleQuack()

simple_duck = Duck(simple_flying_obj, simple_quacking_obj)
print("Simple Duck")
print("\n")
print(simple_duck.fly())
print("Simple Duck Flying")
print("\n")
print("Simple duck quacking")
print(simple_duck.quack())


jet_flying_obj = JetFlying()
loud_quack_obj = LoudQuack()

hybrid_duck = Duck(jet_flying_obj, loud_quack_obj)

print("Hybrid Duck")
print("\n")
print(hybrid_duck.fly())
print("Hybrid Duck Flying")
print("\n")
print("Hybrid duck quacking")
print(hybrid_duck.quack())