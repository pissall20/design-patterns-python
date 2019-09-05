from abc import ABC, abstractmethod


"""
1) The average method is the template method. Observe that it calls at some point all the declared abstract methods, thus, any concrete class that inherits from AverageCalculator must implement them.
2) The has_next abstract method has the following contract: it returns True if the current data source object is able to produce at least one more item, otherwise returns False.
3) The next_item abstract method has the following contract: it returns the next available item from the current data source object. The result is undefined if there are no more available items.
4) The dispose method has the following contract: it will be called in order to free any resources when all the items from the current data source object have been consumed. The default implementation does nothing and doesn’t have to be overridden (because is not decorated with @abstractmethod).
"""
class AverageCalculator(ABC): 

    def average(self): 
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self): 
        pass

    @abstractmethod
    def next_item(self): 
        pass

    def dispose(self): 
        pass
    

"""
The FileAverageCalculator class extends AverageCalculator and represents a source of sequential numerical data obtained from a text file provided during the construction of the object.
"""
class FileAverageCalculator(AverageCalculator):

    def __init__(self, file): 
        self.file = file
        self.last_line = self.file.readline() 

    def has_next(self):
        return self.last_line != '' 

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline() 
        return result

    def dispose(self):
        self.file.close()

"""
Write a new class called MemoryAverageCalculator, which must inherit from the AverageCalculator class. This new class should be a source of sequential numerical data obtained from a list provided during the construction of the object.
"""
class MemoryAverageCalculator(AverageCalculator):

    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def has_next(self):
        return self.index < len(self.lst)

    def next_item(self):
        result = self.lst[self.index]
        self.index += 1
        return result

    def dispose(self):
        pass

# fac = FileAverageCalculator(open('data.txt'))
# print(fac.average()) # Call the template method

# mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
# print(mac.average())



"""
We want to use the Average Calculator code defined previously to compute the average of a sequence of numbers produced by a generator expression. The most obvious option would be to keep using the Template Method design pattern: create a new class that extends the AverageCalculator abstract base class and then implement all its abstract methods. But let’s take a different approach in order to demonstrate how to use the Adapter pattern.

We already have the FileAverageCalculator class that knows how to process sequential numerical data obtained from a text file. Note that both a text file and a generator work practically the same way: you access their elements sequentially, but with a catch. For the text file you call the readline method, yet for the generator you call the next function. So, they have the same behavior, but with a different interface. This is a job for the Adapter pattern.

Reviewing the code of the FileAverageCalculator class we can see that it only uses two methods specific to a text file object: readline and close. So an adapter class would only need to provide these two methods, plus the __init__ method to do any required initialization. With this information we can now define the GeneratorAdapter class:
"""

class GeneratorAdapter:

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ''

    def close(self):
        pass

"""
The __init__ method receives the generator it will be adapting (a.k.a. the adaptee) and stores it in an instance variable.
The readline method delegates its job to the adaptee by calling the next function.
The readline contract establishes that when the end of the file has been reached it should return an empty string. For a generator, the equivalent of an “end of file” is when it can no longer generate more elements. The next function raises a StopIteration exception when called with an exhausted generator.
A generator has no equivalent “closing” operation, yet we do need to provide a close method even if it does nothing because the FileAverageCalculator.dispose method calls it.
"""


from random import randint

g = (randint(1, 100) for i in range(1000000))
fac = FileAverageCalculator(GeneratorAdapter(g))
print(fac.average())
