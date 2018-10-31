-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                contact VARCHAR(50) NOT NULL,
                role VARCHAR(10) NOT NULL,
                password VARCHAR(25) NOT NULL
            )