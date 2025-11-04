

%%sql
ALTER TABLE partidos_camara
    ALTER COLUMN id_partido TYPE BIGINT;

ALTER TABLE partidos_camara
    ADD CONSTRAINT pk_partidos PRIMARY KEY (id_partido);