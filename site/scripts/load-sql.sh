#!/bin/bash

# Directory containing your SQL files
SQL_FILES_DIR="data"

# SQLite database file
DB_FILE="sql_app.db"

# Function to load SQL files into the database
load_sql_files() {
  for sql_file in "$SQL_FILES_DIR"/*.sql;
  do
    echo "Loading $sql_file into $DB_FILE"
    sqlite3 "$DB_FILE" < "$sql_file"
  done
}

# Function to inspect the contents of the tables
inspect_tables() {
  # List all tables
  tables=$(sqlite3 "$DB_FILE" ".tables")

  # Loop through each table and print its contents
  for table in $tables;
  do
    echo "Contents of table $table:"
    sqlite3 "$DB_FILE" "SELECT * FROM $table LIMIT 10;" # Limiting to 10 rows for readability
    echo
  done
}

# Load SQL files and inspect tables
load_sql_files
inspect_tables
