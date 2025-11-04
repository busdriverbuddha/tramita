-- ### 3.1.18 Deputados e órgãos

%%sql
ALTER TABLE deputados_orgaos_camara
    ALTER COLUMN id_deputado_orgao TYPE BIGINT;

ALTER TABLE deputados_orgaos_camara
    ADD CONSTRAINT pk_deputado_orgao
    PRIMARY KEY (id_deputado_orgao);