## Unit testing
Unit testing is a great approach to minimizing bugs in your code.

There is an approach called Test Driven Development (TDD) which takes this to
the extreme.  Here you write tests beforehand which describe the expected
behavior of your code.


## Questions
### The prime bug report
As the author of a popular library called [`prime.py`](prime.py) you
occasionally receive bug reports from users who are using your library in their
application. The latest bug report was filed by someone using [`application.py`](application.py).

1. Run their code and reproduce the error (it should be a math domain error).
2. Examine their code and find the bug.  
3. Now fix your library such that the  application code works correctly (and
    without any other errors).
4. Write one (or more) unit tests to ensure that the bugs that you have fixed
are not reintroduced.
5. Bring your code to class ready to discuss it.

### More defensive testing
Another useful tool in TDD is the notion of code coverage.  

1. Install coverage with `pip3 install coverage`
2. Run the coverage tool on [`test.py`](test.py), and generate the html report.
3. Using the coverage report, write more tests so that you achieve 100% code
coverage.  Does this find anymore bugs in the library?
5. Bring your code to class ready to discuss it.  Be sure to remember which
tests you added from the coverage tool and which tests were introduced from the
original bug report.

### Class project
For your class project write at least 5 unit tests which test the functionality
that you expect to have in any part of the system.  Since these tests will help
you ensure a working project it is in your own interests not to duplicate tests
already written by other students.  So you are encouraged here to collaborate
and maximize your expected coverage. (In some situations there might be limited
scope for unit tests, so there is no penalty for writing duplicate tests.)

Notice that you don't need to have written any functionality for the class
project, in order to start writing the unit tests.  Remember to run the tests
when you do start implementing the functionality.  Seeing a gradual increase in
the number of tests passing can be very motivating!

Bring your unit tests to class and be ready to discuss them.

### (Optional) Optimization of prime library

In the library there have been several attempts at optimization.  For example
the get_next_prime function tests whether the initial x is even and increments
x if it is.  This allows us to only test the odd numbers (we know that an even
number is not prime).

Time the code with and without the optimizations.  Which optimizations give
noticeable speed improvements?  Rewrite `prime.py` using only optimizations that
work. Keep the new code as simple as possible.   Which code would you rather
maintain?

### (Optional) Probabilistic prime tests

In practice the deterministic tests for prime number are too slow.  So as good
engineers, we have decided to trade correctness for speed.  In the new library
we will implement a probabilistic test for primality.  

- Find code online for performing a single probabilistic prime test.
- Decide on a probability of error that you feel comfortable with.
- Now implement the new library such that you can produce primes with a
probability of error not less than your acceptable level.
- What sort of speed is your new library?  How does this compare with the old
library?  Which would you prefer to use for a *really* important cryptographic
purpose?
- How do you test a library that is probabilistic in nature?
- Come and discuss your results with me during office hours!
