-- Select the project database
USE careplus_db;

-- Check total support ticket records
SELECT COUNT(*) AS total_ticket_records
FROM support_tickets_processed;

-- Preview support ticket records
SELECT *
FROM support_tickets_processed
LIMIT 10;

-- Inspect the table columns
DESCRIBE support_tickets_processed;