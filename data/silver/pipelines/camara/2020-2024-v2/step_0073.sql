-- ### 3.1.19 Eventos e órgãos

%%sql
ALTER TABLE eventos_orgaos_camara
    ALTER COLUMN id_evento_orgao TYPE BIGINT;

ALTER TABLE eventos_orgaos_camara
    ADD CONSTRAINT pk_evento_orgao
    PRIMARY KEY (id_evento_orgao);