## SQLAlchemy
SQLAlchemy is a object-relational-mapper (ORM).  This means that it is able
to map from object-oriented code that you write in Python into SQL commands
that a database understands.

This layer of abstraction can allow an engineer to focus on writing good
object-oriented code, while SQLAlchemy will then map this into easy access on a
database.  Having a layer of abstraction allows one to easily change the
underlying database.  It is common for testing code to use a SQLite database,
while in production the code instead connects to a beefy server that is
able to satisfy many simultaneous queries coming from many machines.

## Questions

### Bank loans
From the bank loan exercise at the beginning of the unit:
1. Rewrite all the `CREATE TABLE` commands for the Clients and Loans tables
to now use SQLAlchemy. The SQLAlchemy commands should also create primary key
and foreign key constraints where appropriate.
2. Rewrite all the `INSERT` commands to now use SQLAlchemy. In particular, you
should hold all the values in a standard Python container (e.g. list,
dictionary, or namedtuple), or a combination of Python containers (e.g. list of
dictionaries).  The insertions should all happen in a single transaction.
3. Rewrite all your `SELECT` queries and `UPDATE` commands to now use
SQLAlchemy.
4. Now that you better understand indexing, modify your python code to also
create indexes on relevant columns so that none of your queries from the
previous question will do a full table scan.


### Online retailer
From the session on transactions:
1. Rewrite all the `CREATE TABLE` commands for the tables contained in
`retail.sql` to now use SQLAlchemy. The SQLAlchemy commands should also create
primary key and foreign key constraints where appropriate.
2. Rewrite all the `INSERT` commands to now use SQLAlchemy. In particular, you
should hold all the values in a standard Python container (e.g. list,
dictionary, or namedtuple), or a combination of Python containers (e.g. list of
dictionaries).  The insertions should all happen in a single transaction.
3. Rewrite all your transactions from the exercise to now use SQLAlchemy.

### Abstraction

1. SQLite is not designed to be a production database for large webservices.
Instead a SQL database like MySQL, or PostgreSQL typically get used
and tend to scale better.  However these are all slightly different SQL
dialects.  So a query that works on SQLite might not work on MySQL.
Estimate how much work you will have to do to move all your queries written in
SQLAlchemy and SQLite to now use MySQL and SQLAlchemy. (Hint: the answer is not
zero.)
2. For the previous exercises on loans and retail, get SQLAlchemy to output
the real SQL commands that it sends to SQLite (this is shown in the recommended
tutorial on SQLAlchemy).  How do these commands compare with the SQL that you
wrote manually?  Identify any differences, and find out why SQLAlchemy has done
it differently.
3. (Optional) Explain how you would implement unit-tests which connect to SQLite
but connect to a proper server in production. This is something that I would
strongly recommend for your group project!
4. (Optional) Investigate any differences in speed between using SQLAlchemy
and using SQLite directly.

### (Optional) Unit of Work
SQLAlchemy uses the unit-of-work design pattern to decide when to send updates to the
database.  Read up on the unit-of-work design pattern, and then look at the
source code of SQLAlchemy where it implements it:

https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/unitofwork.py

Now write a very high-level python implementation which captures the essential
idea behind the design, while skipping over much of the complexity in a real
implementation.
