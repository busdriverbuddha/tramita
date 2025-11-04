

%%sql
ALTER TABLE blocos_camara
    ALTER COLUMN id_bloco TYPE BIGINT;

ALTER TABLE blocos_camara
    ADD CONSTRAINT pk_blocos PRIMARY KEY (id_bloco);