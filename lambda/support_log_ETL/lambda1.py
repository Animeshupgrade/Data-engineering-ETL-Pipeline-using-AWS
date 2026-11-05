
import json
import boto3
import re
import pandas as pd
import io
import pyarrow as pa
import pyarrow.parquet as pq


# -------------------------------
# STEP 1: EXTRACT
# -------------------------------

def read_log_from_S3(bucket, key):

    s3 = boto3.client('s3')

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    raw_logs = response['Body'].read().decode('utf-8')

    return raw_logs


# -------------------------------
# STEP 2: TRANSFORM
# -------------------------------

def parse_logs(raw_logs):

    pattern = r'''
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})
    \s+\[(?P<level>[^\]]+)\]
    \s+(?P<service>\S+)
    \s+-\s+
    TicketID=(?P<ticket_id>\S+)
    \s+SessionID=(?P<session_id>\S+)
    \s+IP=(?P<ip>[\d.]+)
    \s*\|\s*
    ResponseTime=(?P<response_time>-?\d+)ms
    \s*\|\s*
    CPU=(?P<cpu>[\d.]+)%
    \s*\|\s*
    EventType=(?P<event_type>\S+)
    \s*\|\s*
    Error=(?P<error>\w+)
    \s+UserAgent="(?P<user_agent>[^"]*)"
    \s+Message="(?P<message>[^"]*)"
    \s+Debug="(?P<debug>[^"]*)"
    \s+TraceID=(?P<trace_id>\S+)
    '''

    parsed_entries = []

    # Split the raw file into individual log records
    entries = raw_logs.split("---")

    for entry in entries:

        entry = entry.strip()

        if not entry:
            continue

        match = re.search(pattern, entry, re.VERBOSE)

        if match:
            parsed_entries.append(match.groupdict())

        else:
            print("Unmatched log entry:", entry[:100])

    df = pd.DataFrame(parsed_entries)

    if df.empty:
        raise ValueError("No log entries could be parsed")

    # Normalize log levels
    level_mapping = {
        "INF0": "INFO",
        "DEBG": "DEBUG",
        "warnING": "WARNING"
    }

    df["level"] = df["level"].replace(level_mapping)

    # Convert numeric columns
    df["cpu"] = pd.to_numeric(df["cpu"])
    df["response_time"] = pd.to_numeric(df["response_time"])

    # Remove trace_id if not required
    df = df.drop(columns=["trace_id"])

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    return df

# STEP 3: LOAD - SAVE AS PARQUET
# -------------------------------

def save_parquet_to_s3(df, bucket, key):

    # Create an in-memory buffer
    buffer = io.BytesIO()

    # Convert Pandas DataFrame to PyArrow Table
    table = pa.Table.from_pandas(df, preserve_index=False)

    # Write the table in Parquet format
    pq.write_table(table, buffer, compression="snappy")

    # Reset buffer position
    buffer.seek(0)

    # Upload Parquet file to S3
    s3 = boto3.client('s3')

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=buffer.getvalue(),
        ContentType="application/vnd.apache.parquet"
    )

    print(f"Parquet file successfully uploaded to s3://{bucket}/{key}")


# -------------------------------
#step4
def lambda_handler(event, context):

    bucket = "an.09-ni"
    key = "support-logs/raw/support_logs_2025-07-01.log"

    # Extract
    raw_logs = read_log_from_S3(bucket, key)

    print("Raw log file successfully extracted")

    # Transform
    df = parse_logs(raw_logs)

    print("Parsed DataFrame:")
    print(df.head().to_string())

    print("Log level distribution:")
    print(df["level"].value_counts().to_dict())

    print("Duplicate count:", df.duplicated().sum())

    # Load - Save as Parquet
    output_key = "support-logs/processed/support_logs.parquet"

    save_parquet_to_s3(df, bucket, output_key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Log ETL completed successfully",
            "total_records": len(df),
            "output_file": output_key
        })
    }

    # -------------------------------



