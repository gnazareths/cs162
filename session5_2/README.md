## Design Patterns - Template and Adapter

### Template - Simulation

The Template pattern is a very powerful
Adapter - StringIO


### Template - Queue
Read up on the implementation of the various Python Queue classes:
https://github.com/python/cpython/blob/3.5/Lib/queue.py

In particular, notice how the `PriorityQueue` and `LifoQueue` have been
implemented.


## Questions

1. Explain the difference between the Facade pattern and and the Adapter pattern

2. Give an example where it will be useful to use the StringIO class

3. From `template.py` implement another class which inherits from
`AbstractSimulation` and performs an interesting simulation.  

4. The queue class is thread safe.  Search the internet to find out what this
means.  What is required to make `put()` and `get()` thread safe?

5. There are many [different variants of Chess](https://en.wikipedia.org/wiki/List_of_chess_variants#Unorthodox_rules_with_traditional_pieces).
Having many different variants with most of the same common functionality lends
itself to the template design pattern.  Implementing the game of chess would be
far too much work.  Instead just sketch out the design that allows many different
variants with a single codebase.  (Assume that both players are human.)
