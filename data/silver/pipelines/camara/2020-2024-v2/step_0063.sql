-- ### 3.1.10 Temas

%%sql
ALTER TABLE temas_camara
    ALTER COLUMN id_tema TYPE BIGINT;

ALTER TABLE temas_camara
    ADD CONSTRAINT pk_temas PRIMARY KEY (id_tema);
