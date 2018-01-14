## ACID and transactions

As a database grows in complexity there tends to emerge natural constraints as
part of the data modeling process. Fortunately SQL provide ACID guarantees,
which can prevent any inconsistencies violating those constraints.  

An example
might be a book exchange database.  Every time two people swap a book then
there are two updates that need to happen. One new entry in the database
showing that book A was given to person 1 from person 2, and another entry
showing that book B was given to person 2 from person 1.  If these two updates
are interrupted halfway through then it will look like book A was given with
nothing given in return.  This would defeat the whole point of a book exchange.
The problem only gets more acute when dealing with money (the books don't
balance).

It is far better to make the updates all-or-nothing (atomic).  This means that
the database is always in a consistent state.  Today's exercises focus on sets
of instructions that must all succeed, or all fail to ensure that the database
is left in a consistent state.

## Questions

### Write-ahead logging
Read up on [write-ahead logging](https://www.sqlite.org/wal.html). Using the
ideas contained there, write out a small example showing several updates being
made to a database using a write-ahead log.  Show that if the update is
interrupted at any point then the database will be able to revert to a
consistent state.

This question does not require any code, but it does require a clear, detailed,
step-by-step description of the process.  

### Online retailer
In `retail.sql` is a possible database design for a large online retail company.
This company has several warehouses, and each warehouse is filled with
several thousand products.  Each product can come from one or more
suppliers, but will only ever be stored in a single warehouse.
Each warehouse has a single delivery company which handles all the
logistics of delivering to a customer.  Fortunately for us, each
customer only has a single address.

The retailer receives orders.  Each order consists of one or more
items to be purchased.  If the item is not available, then it will be
automatically ordered from the cheapest supplier.  

Here is an example transaction for all the needed updates when Gertrud orders
a single widget from us, and we still have sufficient stock in the ABC warehouse:
```SQLite
BEGIN TRANSACTION;
INSERT INTO Orders VALUES (1001, 2000, "2025-01-01 10:00:00", 202501);
INSERT INTO OrderItems VALUES (1001, 3001, 1);
UPDATE Inventory SET Quantity = Quantity - 1 WHERE WarehouseID=4001 AND ProductID=3001;
SELECT Quantity FROM Inventory WHERE WarehouseID=4001 AND ProductID=3001;
END TRANSACTION;
```
Notice that at the end we do a select to double check that we still have
sufficient stock in the warehouse.  (If there were a negative amount, then we
might have to rollback the transaction and order from the suppliers instead.)

Now answer the following:
1. Add all the primary key and foreign key constraints. (This will probably
require you to also reorder some of the table declarations.)
1. Write a transaction for a delivery from the Widge supplier which has just
arrived at the ABC warehouse and unloaded 99 new Widgets.
2. Write a transaction for a Customer order of 500 Wodgets which places an order
with the cheapest supplier.  (Be sure to find the cheapest supplier
automatically, rather than hardcoding your answer.)
3. What statements would be needed to update a customer's details to their new
address, while still maintaining referential integrity?
4. What steps would we need to take to delete a product from the Product table,
while still maintaining referential integrity?  Put all of these statements
together into a transaction.  What collateral damage would be done if a product
was deleted?  (In practice, a product will almost never get deleted unless it
has never been referenced in any other table.)
5. Critique the database design.  What data should be in the database schema,
but isn't?


### Stock trading data
Your company has subscribed to a share trading data feed from the NYSE.  This
data feed lists all the orders placed and all the sales that occur.  
Some orders get cancelled before they can be filled.  

Each order is either to buy or sell a certain number of shares in a particular
company.  The order lists which trading desk placed the order, and if the order is
filled then the trading desk that filled the order is also listed.

At the beginning of the year, your company also received a snapshot of which
trading desks owned which stocks for all the companies listed on the NYSE.
By using the snapshot as a starting point, one can use the successful trades
to update your estimate of all the trading desk portfolios.

As an example, if you knew that the Delta Trading desk had 100 shares of XOM,
and the feed showed another purchase of 100 shares then you knew that Delta
Trading now had 200 shares.

As part of its corporate strategy, your company monitors everyone's portfolios
on a daily basis.  It also monitors the number of sell orders and the number
of buy orders placed by a trading desk every day for every company on the NYSE.

All the orders also get rolled into summary tables for each company.  These
summary tabes list the total number of orders placed, the total number of
orders filled, the total number of shares exchanged, the total number of
dollars exchanged, the minimum price, and the maximum price. This summary
is generated on a daily basis for every company.

1. Design all the SQL tables you need to capture the above requirements.
2. Write the `CREATE TABLE` statements to implement your design.
3. `INSERT` some example data that you have made up.
4. Now write a transaction that updates the portfolios for both the selling
company and the buying company.  This must also then update the summary tables.
5. What would happen if the statements were not wrapped in a transaction, and
everything went smoothly?  What would happen if the set of updates were
interrupted halfway through?

(This is not intending to be a very realistic question, but more a question
around data modeling, and transactions!)
