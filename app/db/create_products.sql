-- Table: public.products

-- DROP TABLE public.products;

CREATE TABLE IF NOT EXISTS public.products
(
  product_id integer NOT NULL DEFAULT nextval('products_product_id_seq'::regclass),
  product character varying(50) NOT NULL,
  quantity integer NOT NULL,
  unit_price integer NOT NULL,
  reg_date timestamp without time zone NOT NULL,
  CONSTRAINT products_pkey PRIMARY KEY (product_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.products
  OWNER TO postgres;
