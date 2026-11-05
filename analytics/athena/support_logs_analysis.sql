-- Select the project database
USE careplus_db;

-- Check total support log records
SELECT COUNT(*) AS total_log_records
FROM support_logs_processed;

-- Preview support log records
SELECT *
FROM support_logs_processed
LIMIT 10;

-- Inspect the table columns
DESCRIBE support_logs_processed;