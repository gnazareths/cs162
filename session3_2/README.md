## Polymorphism
<!-- e.g. The verb "charge" could apply to:
 - horsemen charging an enemy
 - policemen charging a criminal
 - batteries charging
 - a credit card being charged

In different settings, the verb will accomplish different things.


Work through the readings and -->


## Questions:
In this seminar, *not* all questions need to be answered. Question 1 *must* be
answered by everyone, but only one of questions 2 and 3 need to be answered.

Find out which question to answer by running
the following:
```bash
$ python3 utils/personal_exercises.py
```
Once you've entered your email address, you will find out whether to answer
question 2 or question 3 for this seminar.

### 1. A base object
Python provides certain functionality to all classes.


At the REPL, typing `type(x)` will show what type of variable `x` is, while `dir(x)` will reveal all the methods that x has.  Investigate the default behavior t.  Examine the behavior that python gives a using the following few lines of code:

```python
class BlankClass(object):
    '''This is a Blank class for CS162.'''
    pass
t = BlankClass()

class ClassWithAttr(object):
    x1 = 1
    x2 = 2

my_attr = ClassWithAttr()
my_attr.x3 = 3
```

Now find out about the following methods:
 1. help(t)
 2. type(t)
 3. dir(t)
 4. hash(t)
 5. id(t)
 6. hasattr(my_attr,'x3')
 7. getattr(my_attr,'x3')
 8. delattr(my_attr,'x3')
 9. vars(my_attr)
10. bool(t)

*Come to class able to give clear explanations of what is going on in each of
the above methods, and when one might use them.*

### 2. Logging
Logging is very useful, and a great example of polymorphism in action.

Read up on the different logging handlers here:
https://docs.python.org/3.5/library/logging.handlers.html#module-logging.handlers

Look at the source code for the logging module here:
https://github.com/python/cpython/blob/3.5/Lib/logging/handlers.py

1. Build up a list of all the classes defined in the logging library, and all
the parent classes that it inherits from.
2. Now choose a class that inherits from logging.Handler and list all the
methods that one can call on that handler.
3. Find a simple online tutorial on logging in Python and work your way through
it.  

*Come to class with your example code and be able to explain both the design
behind the logging module, and how polymorphism helps build a flexible logging
library.*

### 3. Graphics in Python
Most graphics in python is done using the bundled Tkinter package (https://docs.python.org/3.5/library/tkinter.html).  

Look at the source code for Tkinter here:
https://github.com/python/cpython/blob/3.5/Lib/tkinter/__init__.py
This is a really long file, so clearly you are not expected to
read every line.  But being able to identify the major classes from a large
file is very useful when starting to work on an existing project.

1. Build up a list of all the classes defined in the tkinter library, and all
the parent classes that it inherits from.
2. Now choose a class that inherits from widget and list all the methods that
one can call on that widget.
3. Find a simple online tutorial on tkinter and build a simple graphical user
interface.  How much of the complexity of the library can be hidden from an
enduser?

*Come to class with your example code and be able to explain both the design
behind the Tkinter library and how polymorphism helps build a flexible graphics
library.*
