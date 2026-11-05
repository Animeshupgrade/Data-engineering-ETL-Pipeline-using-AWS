CarePlus – AWS Data Engineering Pipeline
Project Overview

CarePlus is an end-to-end data engineering project designed to process support application logs and customer support ticket data using AWS services.

The project demonstrates data ingestion, ETL processing, cloud storage, data transformation, analytical querying, and dashboard development.

Business Problem

Support systems generate application logs and ticket records that can be difficult to analyze in their raw formats.

This project builds a cloud-based data pipeline to transform raw data into structured, analytics-ready datasets for monitoring and business analysis.

Architecture

CarePlus AWS Architecture

Technology Stack
Category	Technologies
Programming	Python, SQL
Database	MySQL
Cloud Platform	AWS
Object Storage	Amazon S3
Serverless ETL	AWS Lambda, IAM
Data Processing	AWS Glue, os, Pandas, sys, psycopg2
Data Format	CSV, Parquet
Data Catalog	AWS Glue Data Catalog
Query Engine	Amazon Athena
Data Warehouse	Amazon Redshift, CloudWatch
Visualization	Microsoft Power BI
Version Control	Git, GitHub
Project Workflow
1. Support Log Pipeline
Ingest raw support application logs into Amazon S3.
Process and parse log records using Python and AWS Lambda.
Clean and normalize the data.
Convert processed records into Parquet format.
Store the processed data in the S3 processed directory.
2. Support Ticket Pipeline
Extract support ticket data from the MySQL database.
Export the extracted records into CSV format.
Upload the raw CSV files to Amazon S3.
Use AWS Glue to clean and transform the ticket data.
Store the transformed data in Parquet format.
3. Pipeline Automation and Incremental Load
The incremental_data_load_log script holds the database connection and performs the incremental data load, so new records are picked up automatically instead of being loaded manually.
A second AWS Lambda function automates dumping the log files in the support-logs/processed/ directory into Parquet format.
As a result, every time new data is ingested into Amazon S3, the corresponding Parquet files are added to support-logs/processed/ automatically.
Result: before the automation was set up, the query output showed 328 records; after setting up the complete pipeline automation, the same query shows 397 records, confirming that the newly ingested data now flows through to the processed layer.
4. Data Catalog and Analytics
Use AWS Glue Crawlers to discover schemas and register tables in the AWS Glue Data Catalog.
Query processed support logs and ticket datasets using Amazon Athena.
Use Amazon Redshift for analytical data warehousing and SQL analysis.
Build Power BI dashboards to visualize analytical insights.
Repository Structure
text
careplus-aws-data-engineering-pipeline/
│
├── architecture/
│   └── careplus_architecture.svg
│
├── lambda/
│   ├── lambda_1.py
│   ├── lambda_2.py
│   └── requirements.txt
│
├── glue/
│   └── glue_job.py
│
├── data_ingestion/
│   ├── mysql_to_csv.py
│   └── incremental_data_load_log.py
│
├── analytics/
│   ├── athena/
│   │   └── queries.sql
│   └── redshift/
│       └── queries.sql
│
├── dashboards/
│   └── screenshots/
│
├── notebooks/
├── docs/
├── tests/
│
├── README.md
└── .gitignore
AWS Storage Structure
text
Amazon S3
│
├── support-logs/
│   ├── raw/
│   └── processed/      <- new Parquet files are added automatically on each ingestion
│
└── support-tickets/
    ├── raw/
    └── processed/
Key Project Components
Automated and serverless data processing with AWS Lambda.
Automated incremental data loading with continuous Parquet generation in support-logs/processed/.
Batch ETL processing using AWS Glue.
Data ingestion from a relational MySQL database.
Structured storage using Parquet format.
Metadata discovery using AWS Glue Crawlers.
Analytical SQL queries using Athena and Redshift.
Business intelligence dashboards using Power BI.
How to Explore This Repository
lambda/ – Support log ingestion and ETL code, including the Lambda that converts processed logs to Parquet.
glue/ – Support ticket ETL implementation.
data_ingestion/ – MySQL data extraction script and the incremental data load script.
analytics/athena/ – Athena SQL queries.
analytics/redshift/ – Redshift SQL queries.
architecture/ – AWS architecture diagram.
dashboards/ – Power BI dashboard screenshots.
notebooks/ – Data exploration and experimentation.
docs/ – Project documentation.
tests/ – Testing resources.
Security and Data Privacy
No AWS access keys or database passwords should be committed.
Sensitive customer information and production datasets are excluded.
AWS services should be accessed using appropriate IAM permissions.
Author

Animesh Bazar