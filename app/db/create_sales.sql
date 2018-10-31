-- Table: public.sales

-- DROP TABLE public.sales;

CREATE TABLE IF NOT EXISTS sales (
            sale_id SERIAL PRIMARY KEY,
            product VARCHAR(50) NOT NULL,
            quantity INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            attendant VARCHAR(50) NOT NULL,
            date timestamp NOT NULL
            )