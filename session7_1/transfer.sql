CREATE TABLE Balances (
    AccountID INT PRIMARY KEY,
    Name TEXT,
    Balance NUMERIC(10,2)
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    FromAccountID INT,
    ToAccountID INT,
    Amount NUMERIC(10,2),
    FOREIGN KEY (FromAccountID) REFERENCES Balances(AccountID),
    FOREIGN KEY (ToAccountID) REFERENCES Balances(AccountID)
);

INSERT INTO Balances VALUES (101, "Chad E. Blair", 100.00);
INSERT INTO Balances VALUES (102, "Michael K. Taylor", 0.00);

-- SEND $100 from Chad to Michael
BEGIN TRANSACTION;
INSERT INTO Payments VALUES (1, 101, 102, 100.00);
UPDATE Balances SET Balance = Balance - 100.00 WHERE AccountID = 101;
UPDATE Balances SET Balance = Balance + 100.00 WHERE AccountID = 102;
COMMIT;

SELECT * FROM Balances;
SELECT * FROM Payments;
