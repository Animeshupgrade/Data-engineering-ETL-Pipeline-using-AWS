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