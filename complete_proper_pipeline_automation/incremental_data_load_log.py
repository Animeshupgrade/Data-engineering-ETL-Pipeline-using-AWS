import psycopg2

REDSHIFT_HOST = 'default-workgroup.730335502147.eu-north-1.redshift-serverless.amazonaws.com'
REDSHIFT_PORT = '5439'
REDSHIFT_DATABASE = 'careplus_db'
REDSHIFT_USER = 'admin'
REDSHIFT_PASSWORD = 'IYMBYgiel083-%'
REDSHIFT_TABLE = 'public.support_logs'
IAM_ROLE = 'arn:aws:iam::730335502147:role/service-role/AmazonRedshift-CommandsAccessRole-20261103T163414'

def lambda_handler(event, context):

    s3_input_path = "s3://an.09-ni/support-logs/processed/support_logs_2025-07-01.parquet"

    #connect to redshift serverless psygopg2

    conn = psycopg2.connect(
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT,
            database=REDSHIFT_DATABASE,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD
    )

    cursor = conn.cursor()

    print("Connected successfully to Redshift!")

    #copy sql query to load data from S3 into redshift table

    copy_sql = f"""
        COPY {REDSHIFT_TABLE}
        FROM '{s3_input_path}'
        IAM_ROLE '{IAM_ROLE}'
        FORMAT AS PARQUET
        REGION 'eu-north-1'
    """

    #execute the query
    cursor.execute(copy_sql)

    #commit the change
    conn.commit()

    #log success
    print(f"Data loaded successfully from {s3_input_path} to {REDSHIFT_TABLE}")

    # close the cursor and connection
    cursor.close()
    conn.close()
