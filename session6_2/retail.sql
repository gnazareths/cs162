.mode column
.headers on

CREATE TABLE Product (
    ProductID INT,
    Title TEXT,
    Description TEXT,
    Price NUMERIC(11, 2),
    Cost NUMERIC(11, 2)
);
CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    DateOrdered DATETIME,
    MonthOrdered INT
);
CREATE TABLE OrderItems (
    OrderID INT,
    ProductID INT,
    Quantity INT
);


INSERT INTO Product VALUES (3001, "Widget", "Widge all your worries away!", 99.95, 23.05);
INSERT INTO Product VALUES (3002, "Wodget", "Wodge all your worries away!", 199.95, 123.05);

INSERT INTO Orders VALUES (1000, 1, "2025-01-01 10:00:00", 202501);
INSERT INTO OrderItems VALUES (1000, 3001, 1);
INSERT INTO OrderItems VALUES (1000, 3002, 2);

SELECT o.MonthOrdered, SUM(oi.Quantity * p.Price) as Revenue FROM Orders o
    JOIN OrderItems oi on o.OrderID = oi.OrderID
    JOIN Product p on oi.ProductID = p.ProductID
    GROUP BY o.MonthOrdered;
