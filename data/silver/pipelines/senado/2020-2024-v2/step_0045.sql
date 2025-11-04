-- ### 3.1.6. Relatorias

%%sql
ALTER TABLE relatorias_senado
    ALTER COLUMN id_relatoria TYPE BIGINT;

ALTER TABLE relatorias_senado
    ADD CONSTRAINT pk_relatoria PRIMARY KEY (id_relatoria);