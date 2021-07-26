```sql
#LOAD DATA INFILE '/var/lib/mysql-files/bank_address_code.csv' 
#INTO TABLE bank_address_code 
#FIELDS TERMINATED BY ','
#ENCLOSED BY '"'
#LINES TERMINATED BY '\n'
#IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/bank_branch.csv' 
INTO TABLE bank_branch 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```