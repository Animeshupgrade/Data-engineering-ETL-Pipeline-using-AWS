# AWS Lambda – CarePlus Support Logs ETL

## Overview

This AWS Lambda function handles the ingestion and ETL processing of CarePlus application support logs.

It reads raw log files from Amazon S3, extracts structured information, performs data cleaning and transformation, converts the processed records into Parquet format, and uploads the output to the processed S3 directory.

## Responsibilities

The Lambda function performs the following operations:

### 1. Extract
- Connects to Amazon S3 using the AWS SDK for Python (`boto3`).
- Reads raw support log files from the S3 raw directory.
- Retrieves the log file content for processing.

### 2. Transform
- Parses log records using Python regular expressions.
- Extracts fields such as timestamp, log level, service, ticket ID, session ID, IP address, response time, CPU usage, event type, error, user agent, and message.
- Normalizes log levels.
- Converts response time and CPU usage into numeric data types.
- Removes unnecessary fields.
- Removes duplicate records.

### 3. Load
- Converts the cleaned Pandas DataFrame into a PyArrow table.
- Writes the data in Parquet format with Snappy compression.
- Uploads the processed Parquet file to Amazon S3.

## S3 Data Locations

| Data Stage | S3 Location |
|---|---|
| Raw Logs | `s3://an.09-ni/support-logs/raw/` |
| Processed Logs | `s3://an.09-ni/support-logs/processed/` |

## Technologies Used

- **AWS Lambda:** Serverless execution of the ETL process.
- **Amazon S3:** Storage for raw and processed log files.
- **Python:** ETL implementation.
- **Boto3:** AWS service interaction.
- **Pandas:** Data cleaning and transformation.
- **Regular Expressions:** Log parsing.
- **PyArrow:** Parquet conversion and Snappy compression.

## Project Workflow

1. Raw support logs are stored in the S3 raw directory.
2. AWS Lambda reads the raw log file.
3. Python parses and cleans the log records.
4. PyArrow converts the cleaned data into Parquet format.
5. The processed Parquet file is uploaded to the S3 processed directory.
6. AWS Glue Crawler discovers the processed data schema and registers the table in the AWS Glue Data Catalog.
7. Amazon Athena queries the processed data for analytics.

## Dependencies

See `requirements.txt` for the Python dependencies required by the function.

## Execution

The Lambda function can be executed using an AWS Lambda test event or an appropriately configured S3 event trigger.

## Output

The output is a structured Parquet file stored in the S3 processed directory, ready for downstream analytics using AWS Glue and Amazon Athena.

## Security

- AWS credentials should not be hardcoded in the source code.
- Use an IAM execution role with appropriate S3 permissions.
- Do not commit confidential logs, credentials, or sensitive customer information to GitHub.