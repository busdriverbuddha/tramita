

%%sql
ALTER TABLE deputados_camara
    ALTER COLUMN id_deputado TYPE BIGINT;

ALTER TABLE deputados_camara
    ADD CONSTRAINT pk_deputados PRIMARY KEY (id_deputado);