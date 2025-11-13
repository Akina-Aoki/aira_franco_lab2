# DuckDB Bike Data Setup

## Problem
When running `duckdb bike_data.duckdb -ui`, the staging schema doesn't exist even though the SQL commands are written.

## Root Cause
The SQL commands need to be **executed** to create the schema in the database. Simply having the SQL code doesn't create the schema - you need to run it.

## Solution

### Method 1: Using the initialization script (Recommended)

1. Make sure you have DuckDB installed
2. Place your CSV files in the `data/` directory
3. Run the initialization script:
   ```bash
   chmod +x init_database.sh
   ./init_database.sh
   ```

This will execute the SQL commands in `init_schema.sql` and create the staging schema with all tables.

### Method 2: Manual execution

Execute the SQL file directly:
```bash
duckdb bike_data.duckdb < init_schema.sql
```

### Method 3: Execute from within DuckDB CLI

1. Start DuckDB:
   ```bash
   duckdb bike_data.duckdb
   ```

2. Execute the SQL file:
   ```sql
   .read init_schema.sql
   ```

## Verification

After running the initialization, verify the schema was created:

```bash
# Check schemas
duckdb bike_data.duckdb -c "SHOW SCHEMAS;"

# Check tables
duckdb bike_data.duckdb -c "SHOW TABLES;"

# List tables in staging schema
duckdb bike_data.duckdb -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'staging';"
```

## Using the UI

After initialization, you can start the UI and the staging schema will be available:
```bash
duckdb bike_data.duckdb -ui
```

## File Structure

```
aira_franco_lab2/
├── data/                    # Directory for CSV files
│   ├── brands.csv
│   ├── categories.csv
│   ├── customers.csv
│   ├── joined_table.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── staffs.csv
│   ├── stocks.csv
│   └── stores.csv
├── init_schema.sql          # SQL commands to create schema and tables
├── init_database.sh         # Helper script to initialize database
└── bike_data.duckdb         # DuckDB database file (created after initialization)
```

## Notes

- The CSV files need to exist in the `data/` directory before running the initialization
- If CSV files are missing, the table creation will fail but the schema will still be created
- You can re-run the initialization script safely - it uses `IF NOT EXISTS` clauses
