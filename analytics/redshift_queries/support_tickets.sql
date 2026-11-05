CREATE TABLE public.support_tickets (
    agent_name VARCHAR(255),
    resolved_at TIMESTAMP,
    num_interactions INTEGER,
    channel VARCHAR(255),
    created_at TIMESTAMP,
    issue_category VARCHAR(255),
    priority VARCHAR(255),
    ticket_id VARCHAR(255),
    status VARCHAR(255)
);



SELECT COUNT(*) FROM public.support_tickets;