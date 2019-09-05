
"""
Refactor the Tigger class into a Singleton following these steps in the tigger module:

1)  Make the Tigger class private by appending to its name a single leading underscore.

2)  Create a private module-scoped variable called _instance and initialize it with None.

3)  Define a function called Tigger that takes no arguments. This function is responsible for creating an instance of the _Tigger class only once and returning a reference to this unique instance every time it gets called. To accomplish this you’ll need to use the _instance variable from the previous point.
"""


class _Tigger:

    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return 'Grrr!'

_instance = None

def Tigger():
    global _instance
    if not _instance:
        _instance = _Tigger()
    return _instance

