# Amazon Athena Analytics

## Database

- Data Catalog: `AwsDataCatalog`
- Database: `careplus_db`

## Tables

| Table | Description |
|---|---|
| `support_logs_processed` | Processed support application logs |
| `support_tickets_processed` | Processed support ticket records |

## Table Creation

Both tables were created using AWS Glue Crawlers. The crawler discovered the schema of the processed data in Amazon S3 and registered the table metadata in the AWS Glue Data Catalog.

Amazon Athena uses these catalog tables to query the processed datasets.

## SQL Files

- `01_support_logs_analysis.sql` — Support log validation and inspection.
- `02_support_tickets_analysis.sql` — Support ticket validation and inspection.
- `03_table_definitions.sql` — Generated table definitions from Athena.

