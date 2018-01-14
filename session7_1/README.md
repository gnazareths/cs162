## Data Normalization
Data normalization refers to the degree to which potentially-shared
information is moved into separate tables.

## Questions

### Definitions of normalization
Search the internet and find good definitions and examples of the following:
- First normal form
- Second normal form
- Third normal form
- Denormalization
- Composite key

### Road racing association
##### Description
You are contracted out to set up a database for an association of road-runners.
They organize many different races through-out the year. Some of the races get
put into different challenges.  So for example, there could be the following
races:
- The ruby marathon
- The bridge challenge
- The sea to mountain sprint
- Flat and fast marathon
- The wine route stroll

And there could be two challenges:
- **The marathon challenge:**
    - the ruby marathon;
    - the flat and fast marathon.
- **The terrain challenge:**
    - the bridge challenge;
    - the sea to mountain;
    - the ruby marathon.

Notice that not all races belong to a challenge, and some races belong to more
than one challenge.  These challenges repeat every year, but
with subtle differences sometimes (e.g. a new race might be included,
or a particular race is unable to be run that year).

The association needs to be able to keep track of which runners entered
which races, and what their running times were.  A few weeks after the
final race in a particular challenge has been run, the results will get
emailed or posted out.

##### Original Design
1. Design all the SQL tables you need to capture the above requirements.
2. Write the `CREATE TABLE` statements to implement your design.
3. `INSERT` some example data that you have made up.
4. Write a SQL query to find the top 3 fastest women runners for a given race.
5. Write a SQL query to find all the runners' email addresses that
successfully finished the marathon challenge.

##### Alternate Design
Make a copy of your original design and make the following changes
1. Introduce a change in your schema that violates third normal form. Be able to
explain what third normal form is and why your change violates it.
2. Introduce another change, but this time violate second normal form.
Be able to  explain what second normal form is and why your change violates it.
3. Carry out another change, but this time violate the first normal form.
Be able to explain what first normal form is and why your change violates it.
4. Change your database schema, by denormalizing two tables that will be
frequently joined.  Will it ever make sense to denormalize your data, and why?

**Bring your design and your alternate design(s) to class and be prepared to
explain them**
