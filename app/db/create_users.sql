-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE IF NOT EXISTS public.users
(
  user_id integer NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
  username character varying(50) NOT NULL,
  contact character varying(50) NOT NULL,
  role character varying(10) NOT NULL,
  password character varying(25) NOT NULL,
  CONSTRAINT users_pkey PRIMARY KEY (user_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.users
  OWNER TO postgres;
