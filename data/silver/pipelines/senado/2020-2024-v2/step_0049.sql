-- ### 3.1.10. Situações

%%sql
ALTER TABLE situacoes_senado
    ALTER COLUMN id_situacao TYPE BIGINT;

ALTER TABLE situacoes_senado
    ADD CONSTRAINT pk_situacao PRIMARY KEY (id_situacao);