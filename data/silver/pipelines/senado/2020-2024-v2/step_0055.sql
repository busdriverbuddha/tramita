-- ### 3.1.15. Autuações

%%sql
ALTER TABLE autuacoes_senado
    ALTER COLUMN autuacao_idx TYPE BIGINT;

ALTER TABLE autuacoes_senado
    ADD CONSTRAINT pk_autuacao PRIMARY KEY (id_processo, autuacao_idx);