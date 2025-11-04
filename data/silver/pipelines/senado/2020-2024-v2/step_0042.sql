-- ### 3.1.3. Partido

%%sql
ALTER TABLE partido_senado
    ALTER COLUMN codigo_partido TYPE BIGINT;

ALTER TABLE partido_senado
    ADD CONSTRAINT pk_partido PRIMARY KEY (codigo_partido);