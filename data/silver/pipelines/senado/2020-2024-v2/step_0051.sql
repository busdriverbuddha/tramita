

%%sql
ALTER TABLE despachos_senado
    ALTER COLUMN id_despacho TYPE BIGINT;

ALTER TABLE despachos_senado
    ALTER COLUMN id_processo TYPE BIGINT;

ALTER TABLE despachos_senado
    ADD CONSTRAINT pk_despacho PRIMARY KEY (id_despacho, id_processo);