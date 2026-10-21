create database Nassau_Canty_db ;
use Nassau_Canty_db;

Create table Nassau_Canty_Distributor (
Row_ID int Primary key,
Order_ID varchar(50),
Order_Date date,
Ship_Date date,
Ship_Mode varchar(50),
Customer_ID int,
Country_Region varchar(50),
City varchar(50),
State_Province varchar(50),
Postal_Code int,
Division varchar(50),
Region varchar(50),
Product_ID varchar(50),
Product_Name varchar(255),
Sales  decimal,
Units int,
Gross_Profit decimal,
Cost decimal,
Profit_Margin decimal,
Sales_Per_Unit decimal,
Cost_Per_Unit decimal,
Profit_Per_Unit decimal,
Lead_Time int,
Order_Year int,
Order_Month varchar(50),
Order_Quarter varchar(50),
Lead_Time_Category varchar(50),
Shipping_Risk varchar(50)
);

