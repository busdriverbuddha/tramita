-- ### 3.1.17 Histórico de deputados

%%sql
ALTER TABLE deputados_historico_camara
    ALTER COLUMN id_deputado_historico TYPE BIGINT;

ALTER TABLE deputados_historico_camara
    ADD CONSTRAINT pk_deputado_historico
    PRIMARY KEY (id_deputado_historico);