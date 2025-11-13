#!/bin/bash
# Script to initialize the DuckDB database with the staging schema
# 
# This script:
# 1. Creates the bike_data.duckdb database if it doesn't exist
# 2. Executes the init_schema.sql file to create the staging schema and tables
#
# Usage: ./init_database.sh

echo "Initializing DuckDB database with staging schema..."

# Execute the SQL file to create schema and tables
duckdb bike_data.duckdb < init_schema.sql

echo "Database initialization complete!"
echo ""
echo "To verify the schema was created, run:"
echo "  duckdb bike_data.duckdb -c \"SHOW SCHEMAS;\""
echo ""
echo "To view tables in the staging schema, run:"
echo "  duckdb bike_data.duckdb -c \"SHOW TABLES;\""
echo "  or"
echo "  duckdb bike_data.duckdb -c \"SELECT * FROM information_schema.tables WHERE table_schema = 'staging';\""
