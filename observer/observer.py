from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, observable, *args):
        pass


class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.__observers:
            observer.update(self, *args)

"""


The following code shows how to use these classes. 
An Employee instance is an observable object (publisher). Every time its salary is modified all its registered observer objects (subscribers) get notified. 
We provide two concrete observer classes for our demo:

    Payroll: A class responsible for paying the salary to an employee.

    TaxMan: A class responsible for collecting taxes from the employee.


"""
class Employee(Observable):

    def __init__(self, name, salary):
        super().__init__()
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
        self.notify_observers(new_salary)


class Payroll(Observer):

    def update(self, changed_employee, new_salary):
        print(f'Cut a new check for {changed_employee.name}! '
            f'Her/his salary is now {new_salary}!')


class TaxMan(Observer):

    def update(self, changed_employee, new_salary):
        print(f'Send {changed_employee.name} a new tax bill!')

"""
A publisher class needs to extend the Observable class.
It’s essential that the we call the __init__ method of the base class (Observable) using the super function. 
Otherwise, the private attribute _observers (the list that will hold this object’s observers) will not be created.
All the subscribers get notified when the salary is updated through its property setter function.
The Payroll and TaxMan classes extend the Observer class because they are subscribers. These classes need to provide the implementation of the update method, which acts as a callback.
"""

 # Demo code to test above code
"""
e = Employee('Siddhesh Pisal', 50000)
p = Payroll()
t = TaxMan()

e.add_observer(p)
e.add_observer(t)

print('Update 1')
e.salary = 60000

e.delete_observer(t)

print('\nUpdate 2')
e.salary = 65000
"""


"""
Write a class called Twitter that inherits from the Observable and Observer classes so that it effectively behaves simultaneously as a publisher and as a subscriber.
Remember that inheriting from two classes is possible in Python because it supports multiple inheritance.
"""

class Twitter(Observer, Observable):

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def update(self, publisher, tweet):
        print(f"{self.name} received a tweet from {publisher.name}: {tweet}")

    def follow(self, account):
        account.add_observer(self)
        return self

    def tweet(self, msg):
        self.notify_observers(msg) 

a = Twitter('Alice')
k = Twitter('King')
q = Twitter('Queen')
h = Twitter('Mad Hatter')
c = Twitter('Cheshire Cat')

a.follow(c).follow(h).follow(q) 
k.follow(q)
q.follow(q).follow(h)
h.follow(a).follow(q).follow(c)

print(f'==== {q.name} tweets ====')
q.tweet('Off with their heads!')
print(f'\n==== {a.name} tweets ====')
a.tweet('What a strange world we live in.')
print(f'\n==== {k.name} tweets ====')
k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
print(f'\n==== {c.name} tweets ====')
c.tweet("We're all mad here.")
print(f'\n==== {h.name} tweets ====')
h.tweet('Why is a raven like a writing-desk?')

