## SQL
For the unit on SQL we will be focusing on SQLite.  This is a small
relational database which saves all all tables from a single database
into a single file.

For the first few sessions, it is recommended that you run sqlite3 directly
through the sqlite3 shell.  Search the internet for help to you get this up
and running for your particular platform.

Once you are able to run commands in the shell then you can begin creating
tables, inserting data and querying the data.  A good approach is to
create a single long text file containing all the commands.  Depending on the
platform the following might work for a file called `create.sql`:
```bash
$ sqlite3 < create.sql
```
This will execute all the commands against an in-memory database.  If you want
the database to persist then you can tell sqlite to store the database in a file:
```bash
$ sqlite3 cs162.db < create.sql
```
If your platform does not support piping in the commands then you will have to
do the following:
```bash
$ sqlite3
SQLite version 3.16.0 2016-11-04 19:09:39
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .read create.sql
```

Remember to comment your SQL commands!  Single line comments use a double
hyphen (`--`), while multi-line comments use `/* ... */`.

## Questions
Answer the questions below. Be sure to bring your SQL code to class
and be ready to share and discuss it.  CoCalc will allow you to upload your
sql script and run it, so also make sure that it displays the data before
running any queries on it.

### Bankloans
In the file `bankloans.sql` you will find sqlite commands that create some
tables and insert some simple data.  We need to query the data, and there are
some descriptions of the needed queries.  
1. Make sure that you can execute the sql file.
2. Now fill in the missing queries!

### Ride-sharing
You are the founder of a ride-sharing startup and need to design the
initial database.

Your startup will be a platform that connects drivers with people who need a
lift.  You will need to keep track of:
- the rides taken,
- billing for riders,
- monthly payments for drivers.

1. Design all the SQL tables you need to capture the above requirements.
2. Write the `CREATE TABLE` statements to implement your design.
3. `INSERT` some example data that you have made up.
4. Write a query to find out how many trips have been made by each driver this
month, and how much they will be paid.
5. Write a query to find all the riders who haven't taken any trips this
month. (So we can send them an irritating marketing email!)
