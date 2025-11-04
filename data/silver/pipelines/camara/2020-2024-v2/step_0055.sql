

%%sql
ALTER TABLE frentes_camara
    ALTER COLUMN id_frente TYPE BIGINT;

ALTER TABLE frentes_camara
    ADD CONSTRAINT pk_frentes PRIMARY KEY (id_frente);