CREATE DATABASE careplus_db;

CREATE TABLE public.support_logs (
    "timestamp" VARCHAR(255),
    level VARCHAR(255),
    service VARCHAR(255),
    ticket_id VARCHAR(255),
    session_id VARCHAR(255),
    ip VARCHAR(50),
    response_time BIGINT,
    cpu DOUBLE PRECISION,
    event_type VARCHAR(255),
    error VARCHAR(65535),
    user_agent VARCHAR(65535),
    message VARCHAR(65535),
    debug VARCHAR(65535)
);

SELECT COUNT(*) FROM public.support_logs;

output: 397 /* first this shows 328 records after setting up proper pipeline this shows 397 */

/*incremental_data_load_log file contain the database coneection 
          
          and another lambda function that automate the task of dumping the 
                                     
                                    log file in processed doirectory into perquet format that's why the new data added into support-logs/processed as much as
                                    
                                                                  I perform data ingestion into S3.*/