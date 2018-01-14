## Unified Modeling Language - Class diagrams

In the last seminar we covered two large software libraries.  Hopefully it
became clear that reading, understanding and discussing a large library can be
tricky and time-consuming.

Part of becoming a good software engineer is learning how to communicate
concepts in a standard way.  By standardizing communication it becomes possible
to use less time and be more precise.

The concepts of how several objects interact together, with shared methods and
non-trivial inheritance is best conveyed using a UML class diagram.

We will use UML diagrams with the following expectations
1. **UML sketching:** while one can use UML diagrams to describe a system in
incredible detail, most of the value from UML comes from sketching the system.
A coarse level description allows a team of engineers to agree on a high-level
design, and split up the necessary work fairly.
2. **Iterative development:** given the fast-paced and fluid nature of software
development, it makes sense to focus on providing enough detail in your UML
diagrams to build only the first two or three features.
3. **Adaptive planning:** As the project gets built out, we will continually
adapt and rework the plan based on feedback from users, as well as our
experience in implementation.

*From this it makes sense to focus on only a small portion of UML: class diagrams
and sequence diagrams (Videos 3 and 4 in the recommended material).  Also, your
solutions needn't be completely detailed, but should capture the essence of the
system.*

## Separation of Concerns
From looking at two standard Python libraries, it has hopefully become clear how
one can design a library in such a way as to separate various concerns.

In the logging library, there are several concerns that have been cleanly
separated:
1. **Handler**: Where should the log message go?
2. **Formatter** How should the log message be formatted?
3. **Filter** Which log messages should be kept?
4. **LogRecord** What information might be needed for a log message?
5. **Logger** Where and when should a log message be created?

By keeping everything so clearly separated it allows for the easy addition of
new features.  If one wants to log messages to a large LED sign above one's
computer, then one just needs to extend the Handler class such that it can send
a message to the sign, and all other existing functionality can be reused.

## Questions

### 1. Tkinter
Search the internet for images using the search term "Tkinter class diagram".
<ol type="a">
<li>Find a useful diagram which explains the structure of the library.</li>
<li>What insights does the diagram provide that you didn't get from reading the
documentation?</li>
<li>What insights would you have to read the documentation to get?</li>
</ol>

### 2. Logging
Draw a class diagram of the Logging library, including some of the logging
handlers, filters, formatters and LogRecord classes. Does this do a better job
of describing the library than you were able to last session?

### 3. Class Project
Using your new insight, decompose your class project into as many classes as you
think you will need.  Draw this proposed solution into a UML diagram, bring it
to class and be prepared to explain your design decisions to your fellow
students.  How well does your design separate out different concerns?

*Discussing your class project question with fellow students before class is
discouraged as we will be interested in the variety of solutions that students
obtained in class.*

### 4. (Optional) Automatic Code analysis
Some tools are able to automatically analyze code and produce class diagrams.
Find a tool which works on python source code, and get it to generate class
diagrams for both the Tkinter library and the logging library.

*If you automatically generate class diagrams for both libraries then that will
count as answering the first two questions in this session.*

### 5. (Optional) Automatic Code generation
Use [StarUML](http://staruml.io/) to generate
[Python code](http://staruml.io/extensions) from your UML description of the
class project.  Look at the quality of code produced.
<ol type="a">
  <li>Is this better or worse than handwritten code?</li>
  <li>How much functionality still needs to be added?</li>
  <li>If your design changes, how much work does it take to rework the UML diagram
  and then regenerate the code?</li>
</ol>
