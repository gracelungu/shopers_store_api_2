-- Table: public.products

-- DROP TABLE public.products;

CREATE TABLE IF NOT EXISTS products (
				product_id SERIAL PRIMARY KEY,
					product VARCHAR(50) NOT NULL,
					quantity INTEGER NOT NULL,
					unit_price INTEGER NOT NULL	
						)