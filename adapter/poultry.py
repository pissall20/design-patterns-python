class Duck:

    def quack(self):
      print('Quack')

    def fly(self):
        print("I'm flying")


class Turkey:

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print("I'm flying a short distance")


"""
You want your turkeys to behave like ducks, so you need to apply the Adapter pattern. In the same file, write a class called TurkeyAdapter and make sure it takes into account the following:

The adapter’s __init__ method should take its adaptee as an argument.

The quack translation between classes is easy: just call the gobble method when appropriate.

Even though both classes have a fly method, turkeys can only fly in short spurts — they can’t do long-distance flying like ducks. To map between a duck’s fly method and the turkey’s method, you need to call the turkey’s fly method five times to make up for it.
"""

class TurkeyAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        self.adaptee.gobble()

    def fly(self):
        for i in range(5):
            self.adaptee.fly()

# Test with the following code:

def duck_interaction(duck):
    duck.quack()
    duck.fly()


duck = Duck()
turkey = Turkey()
turkey_adapter = TurkeyAdapter(turkey)

print('The Turkey says...')
turkey.gobble()
turkey.fly()

print('\nThe Duck says...')
duck_interaction(duck)

print('\nThe TurkeyAdapter says...')
duck_interaction(turkey_adapter)
