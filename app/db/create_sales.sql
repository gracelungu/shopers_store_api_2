-- Table: public.sales

-- DROP TABLE public.sales;

CREATE TABLE IF NOT EXISTS public.sales
(
  sale_id integer NOT NULL DEFAULT nextval('sales_sale_id_seq'::regclass),
  product character varying(50) NOT NULL,
  quantity integer NOT NULL,
  amount integer NOT NULL,
  attendant character varying(50) NOT NULL,
  date timestamp without time zone NOT NULL,
  CONSTRAINT sales_pkey PRIMARY KEY (sale_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.sales
  OWNER TO postgres;
