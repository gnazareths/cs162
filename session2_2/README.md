# Session 2.2

### 1. Get started
To set up a suitable environment for this session's code:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python blackjack.py
```
And you should be able to play a simplified form of blackjack.

### 2. Read `blackjack.py`
(and identify why it is poorly-designed)

This is a badly-architected procedural program. The exercise for today's seminar is to refactor this program into a well-designed, object-oriented program.  Labeling a program as object-oriented does not make it inherently good, and what follows is a short justification of why we should care about good design and object-orientation.

For this course, we will define a program to be well designed iff:
>There are many potential features that could be added to the program, and each feature only requires a small number of locations to edited.

This is arguably *the* key aspect of good design.  It is the only requirement that allows a project to grow in scale and complexity.  If you have a project of millions of lines of code (e.g. the linux kernel, a modern web-browser) then good design is essential.  Consider a large project that is badly designed (ie. adding a single feature usually affects the entire codebase) then progress will necessarily be very slow.  Not only will an engineer need to understand millions of lines of code, but they will also need to synchronously make changes in many locations (to avoid introducing bugs).  This bad project also has the side effect that whenever one new feature is rolled out by another team then it will most likely affect the progress of all other teams ("stepping on each other's toes").

The thing that can save us is the notion of abstraction.  We can break down a large project into many small subsystems.  Each subsystem can hide the complexity of the implementation from other subsystems. This decouples what a subsystem does from how it does it.  

This notion of good design doesn't necessarily lead us into object-oriented principles, and there have been other interesting approaches (eg. google functional programming techniques).  However historically object-orientation has been the most successful and scaled to the largest projects.

Phew! That was quite a long aside.  Let's get back to today's task of getting a better codebase for our little Blackjack project.  This is a poorly designed project because all sorts of things are done all over the place.

### 3. Use a better random number generator

In a real project we would (and should) use the facilities provided by python in the `random` module. However this will give you the opportunity to design a simple class and see how the refactored code is (hopefully) simpler and better separated.

It turns out that [RANDU](https://en.wikipedia.org/wiki/RANDU) is actually a bad random number generator (and RANDU was used by many real scientific computing centers for over a decade).  A better choice is to use a lagged fibonacci generator (which is what is actually used in the `random` module).

There is some example code for you to use in the file `mersenne.py` (this python code is adapted from
[here](http://code.activestate.com/recipes/578056-mersenne-twister/)).

Identify the following:
1. The current implementation refers to the data for the random number generator in many lines.  Identify each line of code where this happens.
2. If we are using a random number generator, what functionality do we actually care about?

Program the following:
1. Build a random number based on the RANDU implementation code that hides as much implementation detail as possible and only exposes the needed functionality.
2. Build a random number generator based on the Mersenne twister code that hides as much implementation detail as possible and only exposes the needed functionality.
3. Refactor your blackjack code so that it uses one of the new random number generator classes and it is easy to swap between either class.

Think about whether there are any leaks in your abstraction of a random number generator.

### 4. Refactor the blackjack code
The current implementation of blackjack has all sorts of poor design choices implicit in the code.  For example a card is represented by a string, and the value of that card depends on the string representation.  However if we wanted to play blackjack in a different language (such as German) the card would have a different representation and the value would be incorrectly calculated.
1. Identify which things in the program would be best represented using a class.  Associate particular data and behaviors with each relevant class.
2. Now implement your design!
3. Is the new design longer or shorter than the old design?
4. Is the new design easier to read than the old design?
5. Is it easier to add a new feature in the new design or the old design?


### 5. Add multiple language support
This is the trickiest part of today's assignment.  Minerva is a very multicultural institution with many different languages being spoken.  While we use English in the classroom, we certainly should accommodate non-native speakers if they want to play blackjack in their leisure time and in their native language.

Make sure that your blackjack game can be played in one or more languages.  The best way to do this is to abstract way how a particular point in the game is presented to the user.

A bad implementation will require a single global variable called language and have code littered with if statements like (please excuse my google translate):

```python
if LANGUAGE == 'en':
    print('You have gone bust!')
elif LANGUAGE == 'de':
    print('Du bist gegangen!')
elif LANGUAGE == 'es':
    print('¡Te has vuelto loco!')
```

A good implementation would ideally allow a translator without any programming knowledge to come in and provide translations for a new language without writing a single line of code.

### 6. (Optional) Implement more Blackjack rules

Find out what the full set of rules are for blackjack.  There are many subtleties that have been left out of the current implementation.  Find one such subtlety and implement it in the refactored codebase.  If you have done a good job of design then adding a new rule should affect a small number of locations in the codebase.  Think about how it would have been implemented in the old design, and whether this is an improvement or not.
