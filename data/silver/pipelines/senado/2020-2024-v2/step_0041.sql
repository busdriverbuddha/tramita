

%%sql
ALTER TABLE parlamentar_senado
    ALTER COLUMN codigo_parlamentar TYPE BIGINT;

ALTER TABLE parlamentar_senado
    ADD CONSTRAINT pk_parlamentar PRIMARY KEY (codigo_parlamentar);