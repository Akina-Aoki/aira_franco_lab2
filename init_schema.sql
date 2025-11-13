/*Create a schema and table to ingest bike data from csv files in one command line

*/

-- First create a schema. Common practice is to name schema as staging
CREATE SCHEMA IF NOT EXISTS staging; 


CREATE TABLE
    IF NOT EXISTS staging.brands AS ( -- create a table named brands in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/brands.csv')  -- specify the path to the csv file
    );


CREATE TABLE
    IF NOT EXISTS staging.categories AS ( -- create a table named categories in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/categories.csv')  -- specify the path to the csv file
    );


CREATE TABLE
    IF NOT EXISTS staging.customers AS ( -- create a table named customers in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/customers.csv')  -- specify the path to the csv file
    );

CREATE TABLE
    IF NOT EXISTS staging.joined_table AS ( -- create a table named joined_table in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/joined_table.csv')  -- specify the path to the csv file
    );


CREATE TABLE
    IF NOT EXISTS staging.order_items AS ( -- create a table named order_items in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/order_items.csv')  -- specify the path to the csv file
    );


CREATE TABLE
    IF NOT EXISTS staging.orders AS ( -- create a table named orders in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/orders.csv')  -- specify the path to the csv file
    );

CREATE TABLE
    IF NOT EXISTS staging.products AS ( -- create a table named products in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/products.csv')  -- specify the path to the csv file
    );

CREATE TABLE
    IF NOT EXISTS staging.staffs AS ( -- create a table named staffs in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/staffs.csv')  -- specify the path to the csv file
    );

CREATE TABLE
    IF NOT EXISTS staging.stocks AS ( -- create a table named stocks in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/stocks.csv')  -- specify the path to the csv file
    );

CREATE TABLE
    IF NOT EXISTS staging.stores AS ( -- create a table named stores in staging schema
        SELECT
            *
        FROM
            read_csv_auto ('data/stores.csv')  -- specify the path to the csv file
    );
