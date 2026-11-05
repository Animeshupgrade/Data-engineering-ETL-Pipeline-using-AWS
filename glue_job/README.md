# AWS Glue ETL – CarePlus Support Tickets

## Overview

This AWS Glue ETL job processes CarePlus support ticket data extracted from the MySQL OLTP database.

The job reads raw CSV files from Amazon S3, performs data cleaning and transformation, converts the data into Parquet format, and stores the processed output in Amazon S3 for downstream analytics.

## ETL Workflow

### 1. Extract
- Reads support ticket CSV files from the S3 raw directory.
- Uses AWS Glue and its underlying Apache Spark processing capabilities to access the source data.

### 2. Transform
- Cleans and prepares support ticket records.
- Handles data type conversions.
- Applies the transformations implemented in the Glue job script.

### 3. Load
- Converts the transformed dataset into Parquet format.
- Writes the processed data to the S3 processed directory.

## S3 Data Locations

| Data Stage | S3 Location |
|---|---|
| Raw Data | `s3://an.09-ni/support-tickets/raw/` |
| Processed Data | `s3://an.09-ni/support-tickets/processed/` |

## Technologies Used

- AWS Glue
- Apache Spark
- PySpark
- Amazon S3
- Python
- Parquet

## Downstream Analytics

The processed Parquet dataset is discovered using an AWS Glue Crawler and registered in the AWS Glue Data Catalog.

Amazon Athena uses the catalog table `support_tickets_processed` to execute analytical SQL queries.

## Repository Files

- `glue_job.py` – AWS Glue ETL implementation.
- `README.md` – Documentation of the Glue ETL process.

## Security

Do not commit AWS credentials, database passwords, confidential customer information, or actual production datasets to GitHub.