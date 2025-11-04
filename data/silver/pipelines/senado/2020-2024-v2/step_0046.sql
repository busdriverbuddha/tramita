-- ### 3.1.7. Votações

%%sql
ALTER TABLE votacoes_senado
    ALTER COLUMN id_votacao TYPE BIGINT;

ALTER TABLE votacoes_senado
    ADD CONSTRAINT pk_votacao PRIMARY KEY (id_votacao);