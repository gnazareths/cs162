.mode column

CREATE TABLE Clients (
    CLIENTNUMBER INT,
    FIRSTNAME VARCHAR(20),
    SURNAME VARCHAR(20),
    EMAIL VARCHAR(100),
    PHONE VARCHAR(20)

);
CREATE TABLE Loans (
    ACCOUNTNUMBER INT, --A unique integer to identify this account
    CLIENTNUMBER INT, -- An integer to identify the client (clients may have more than one account)
    STARTDATE DATETIME, -- The time that this account was created
    STARTMONTH INT, -- The month for which the first repayment is due (201805 means May 2018)
    TERM INT, -- Over how many months the loan must be repaid
    REMAINING_TERM INT, -- How many months remain
    PRINCIPALDEBT NUMERIC(11, 2), -- The size of the initial loan
    ACCOUNTLIMIT NUMERIC(11, 2), --
    BALANCE NUMERIC(11, 2), -- How much is currently owed
    STATUS VARCHAR(11) -- Human readable status - e.g. "PAID OFF", "ARREARS", "NORMAL"
);

INSERT INTO Clients VALUES (1, 'Robert', 'Warren', 'RobertDWarren@teleworm.us', '(251) 546-9442');
INSERT INTO Clients VALUES (2, 'Vincent', 'Brown', 'VincentHBrown@rhyta.com', '(125) 546-4478');
INSERT INTO Clients VALUES (3, 'Janet', 'Prettyman', 'JanetTPrettyman@teleworm.us', '(949) 569-4371');
INSERT INTO Clients VALUES (4, 'Martina', 'Kershner', 'MartinaMKershner@rhyta.com', '(630) 446-8851');
INSERT INTO Clients VALUES (5, 'Tony', 'Schroeder', 'TonySSchroeder@teleworm.us', '(226) 906-2721');
INSERT INTO Clients VALUES (6, 'Harold', 'Grimes', 'HaroldVGrimes@dayrep.com', '(671) 925-1352');

INSERT INTO Loans VALUES (1,1,'2017-11-01 10:00:00', 201712, 36, 35, 10000.00, 15000.00, 9800.00, 'NORMAL');
INSERT INTO Loans VALUES (2,2,'2018-01-01 10:00:00', 201802, 24, 24, 1000.00, 1500.00, 1000.00, 'NORMAL');
INSERT INTO Loans VALUES (3,1,'2016-11-01 10:00:00', 201612, 12, -3, 2000.00, 15000.00, 4985.12, 'ARREARS');
INSERT INTO Loans VALUES (4,3,'2018-01-01 10:00:00', 201802, 24, 24, 3500.00, 5000.00, 1300.00, 'NORMAL');
INSERT INTO Loans VALUES (5,4,'2017-11-01 10:00:00', 201712, 12, 35, 10000.00, 15000.00, 0.00, 'PAID OFF');
INSERT INTO Loans VALUES (6,5,'2018-01-01 10:00:00', 201802, 48, 24, 1000.00, 1500.00, 0.00, 'PAID OFF');
INSERT INTO Loans VALUES (7,6,'2015-11-01 10:00:00', 201512, 12, -20, 10000.00, 15000.00, 9800.00, 'Arrears');
INSERT INTO Loans VALUES (7,4,'2018-01-01 10:00:00', 201802, 12, 1, 2400.00, 3600.00, 130.00, 'NORMAL');

-- Is the data there?
SELECT 'Loans';
SELECT '----------------------------------------------------';
SELECT * FROM Loans;
SELECT '';
SELECT 'Clients';
SELECT '----------------------------------------------------';
SELECT * FROM Clients;

SELECT '1. Everyone who owes more than $5,000 on an account:';
SELECT '----------------------------------------------------';
SELECT FIRSTNAME, SURNAME, BALANCE FROM Loans
    JOIN Clients ON Loans.CLIENTNUMBER = Clients.CLIENTNUMBER
    WHERE BALANCE > 5000.00;

SELECT '';
SELECT '2. Find all loans older than Jan 2017';
SELECT '----------------------------------------------------';

SELECT '';
SELECT '3. Find all clients who have more than one loan';
SELECT '----------------------------------------------------';

SELECT '';
SELECT "4. Find the total balance outstanding over all loans that aren't in arrears";
SELECT '----------------------------------------------------';

SELECT '';
SELECT '5. Are all account numbers unique? (How should we fix this in general)';
SELECT '----------------------------------------------------';

SELECT '';
SELECT '6. Martina has undergone gender reassignment and is now Martin';
SELECT '----------------------------------------------------';

SELECT '';
SELECT '7. Get a list of email addresses for all clients who paid off a loan';
SELECT '----------------------------------------------------';

SELECT '';
SELECT '8. Print out the largest loan for each client';
SELECT '----------------------------------------------------';
