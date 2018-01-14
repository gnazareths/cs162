## Inheritance vs Composition
Today's reading and exercises will help you better understand when to use inheritance and when to use object composition.

### Inheritance
Consider the following objects:

```python
class Fruit():
    def __init__(self, name, weight_kg):
        self.name = name
        self.weight_kg = weight_kg
        self._ripe = False
        self._rotten = False

    def __repr__(self):
        return "{} ({:.3f}kg)".format(self.name, self.weight_kg)

    def ripen(self):
        if ~self._rotten:
            self._ripe = True
            print("{} is ready to eat!".format(self.name))

    def neglect(self):
        self._rotten = True
        print("Now {} is rotten :'-(".format(self.name))

    def ready_to_eat(self):
        return self._ripe and not self._rotten


class Banana(Fruit):
    def __init__(self, name='Banana', weight_kg=0.2):
        super().__init__(name, weight_kg)
        self._peeled = False

    def peel(self):
        self._peeled = True

    def ready_to_eat(self):
        if self._peeled:
            return super().ready_to_eat()
        return False


s = Fruit('Strawberry', 0.05)
a = Fruit('Apple', 0.25)
b = Banana()
s.ripen()
a.neglect()
b.ripen()
b.peel()
```
By inheriting from Fruit, Banana gets all of the functionality that fruit
provides, and is able to extend that functionality as well.
We also implement the `__repr__` method so that we are able to print human-
readable representations of our objects.  Python follows a convention that any
methods or variables which begin with a single underscore (e.g. `_ripe`) are
for private use by the class, and should not be called from outside the class (
although it is possible to do so).  Methods that begin and end with a double
underscore (e.g. `__repr__`) are methods that are built into the language.

Being able to inherit and extend large amounts of functionality
is a major benefit of object oriented programming, but it must be used with
care.  In the above example there is already a subtle issue creeping in, before
a banana is ready to eat it must be peeled.  When b.ripen() is called the
method prints that the banana is ready to eat. This is a a violation of the
Liskov Substitution principle, which states that any subtype *must* be able to
be substituted for its parent and function correctly in any situation that the
parent functions correctly.

So while this example is trivial and the extra conditions are easily remembered,
as the project grows in size and complexity this violation can be a source of
bugs for any programmer using these objects.

### Composition
Another way to use objects is to add them as member variables of a class:

```python
class Chef():
    def __init__(self):
        self.fruit = []

    def ripen(self):
        for f in self.fruit:
            f.ripen()

    def neglect(self):
        for f in self.fruit:
            f.neglect()

    def get_ready_to_eat(self):
        return [f for f in self.fruit if f.ready_to_eat()]

    def get_not_ready_to_eat(self):
        return [f for f in self.fruit if not f.ready_to_eat()]

    def get_fruit_salad(self):
        ans = []
        for f in self.get_ready_to_eat():
            (num_slices, remainder) = divmod(f.weight_kg, 0.05)
            for a in range(int(num_slices)):
                ans.append(Fruit(f.name + ' Slice', 0.05))
            if remainder > 1e-16:
                ans.append(Fruit(f.name + ' Slice', remainder))
        self.fruit = self.get_not_ready_to_eat()
        return ans


chef = Chef()
chef.fruit = [s, a, b]
if isinstance(chef, Fruit):
    print("Chef is type of a Fruit??")
else:
    print("Chef is not a type of Fruit")

print(chef.get_fruit_salad())
```
Now it is clear that a chef isn't a type of fruit (it doesn't
inherit from Fruit).  Also there are methods that Fruit has which Chef
doesn't have (`ready_to_eat`).  This can make it clearer when it is appropriate
for a Chef and when it is appropriate for Fruit.

As an  aside, in Python is it usually the case that one doesn't explicitly test
whether or not an instance is a subclass of something.  Instead just call the
methods that it is supposed to have implemented. This is known as "duck typing",
if it walks like a duck, and it talks like a duck, then it's probably a duck.

### Multiple Inheritance
Python allows the powerful notion of multiple inheritance.  This allows for the
implementation of things like tomatoes which are both a fruit and a vegetable.

```python
from enum import Enum


class Cooked(Enum):
    BOILED = 1
    FRIED = 2
    ROAST = 3


class Vegetable():
    def __init__(self, name):
        super.__init__()
        self.name = "Vegetable " + name
        self.cooked = None
        print("Vegetable Initialized")

    def fry(self):
        self.cooked = Cooked.FRIED


class Tomato(Fruit, Vegetable):
    def __init__(self, name='Tomato', weight_kg=3.0):
        super().__init__(name=name, weight_kg=weight_kg)


t = Tomato()
print(t)
```

## Questions:
### 1. Multiple inheritance bug
There is a subtle bug in the initialization of a tomato.  Identify the bug,
and then fix the bug!

### 2. Bug or feature?
Notice that a tomato can now also appear inside a fruit salad without any
errors.  Is this a bug or a feature?  Make arguments for both sides.

### 3. Identity Access Management - IAM
It is crucial to get the access control correctly implemented.  As an example,
consider logging onto ALF.  In this case there are students and professors, each
of whom is part of multiple courses.  In each course one might have different
roles - e.g. a professor might be a teacher in one class, while taking another
class as a student.  Professors are able to do more things on the platform than
students, e.g. send the class to breakout.  There might be other actions as
well, for example some students might be privileged with the option of enabling
or disabling student drawing on slides.  When things break (as they sometimes
do), then it will be really useful to have people with tech support privileges
come into any class and perform any action.

 Design a system which represents all parts of the problem and can flexibly
assign students and professors to new classes. The system must also be able
to efficiently determine whether a person is able to perform a particular
action, such as sending the class to breakout.

 (The model sketched out here is more flexible than the actual policy
implemented in ALF.  As an alternative exercise, try to design how IAM is handled
in ALF.)

### 4. Liskov Substitution principle
 At the REPL, typing `type(x)` will show what type of variable `x` is, while `dir(x)` will reveal all the methods that x has.

 Work through the simple types (e.g. list, int, float, string) and find out whether it is possible to call the following code with an instance of that type.  Is it possible to find an instance that works, while another instance (of the same type) fails?  

```python3
def liskov_substitution_principle(x):
    x = x % x
    x = x * 2
    print(x)
```
 Is this a violation of the Liskov substitution principle? Why or why not?

 [Helpful reading](https://docs.python.org/3.5/library/operator.html)
