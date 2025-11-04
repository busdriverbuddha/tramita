

%%sql
ALTER TABLE eventos_camara
    ALTER COLUMN id_evento TYPE BIGINT;

ALTER TABLE eventos_camara
    ADD CONSTRAINT pk_eventos PRIMARY KEY (id_evento);