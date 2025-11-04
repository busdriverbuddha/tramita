-- ### 3.1.4. Processo

%%sql
ALTER TABLE processo_senado
    ALTER COLUMN id_processo TYPE BIGINT;

ALTER TABLE processo_senado
    ADD CONSTRAINT pk_processo PRIMARY KEY (id_processo);