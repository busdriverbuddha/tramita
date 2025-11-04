-- ### 3.1.12. Outros números

%%sql
ALTER TABLE outros_numeros_senado
    ALTER COLUMN id_outro_numero TYPE BIGINT;

ALTER TABLE outros_numeros_senado
    ADD CONSTRAINT pk_outro_numero PRIMARY KEY (id_outro_numero);