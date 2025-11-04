

%%sql
ALTER TABLE encontro_legislativo_senado
    ALTER COLUMN id_encontro_legislativo TYPE BIGINT;

ALTER TABLE encontro_legislativo_senado
    ADD CONSTRAINT pk_encontro_legislativo PRIMARY KEY (
        id_encontro_legislativo
    );