-- ### 3.1.14. Processos relacionados

%%sql
ALTER TABLE processos_relacionados_senado
    ALTER COLUMN id_processo_relacionado TYPE BIGINT;

ALTER TABLE processos_relacionados_senado
    ADD CONSTRAINT pk_processo_relacionado PRIMARY KEY (id_processo_relacionado);