
create_table = '''CREATE TABLE public."user" (
	id serial4 NOT NULL,
	"name" varchar NOT NULL,
	"desc" varchar NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
'''



insert_user = '''insert into "user" ("name", "desc") VALUES ('Oleskii', 'QA') returning "id";'''



update = '''UPDATE "user" set name = 'Den' where "id" = 2'''