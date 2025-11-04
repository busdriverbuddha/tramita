

%%sql
ALTER TABLE orgaos_camara
    ALTER COLUMN id_orgao TYPE BIGINT;

ALTER TABLE orgaos_camara
    ADD CONSTRAINT pk_orgaos PRIMARY KEY (id_orgao);