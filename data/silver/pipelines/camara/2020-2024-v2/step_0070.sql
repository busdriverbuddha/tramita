-- ### 3.1.16 Deputados e frentes

%%sql
ALTER TABLE deputados_frentes_camara
    ALTER COLUMN id_deputado_frente TYPE BIGINT;

ALTER TABLE deputados_frentes_camara
    ADD CONSTRAINT pk_deputado_frente
    PRIMARY KEY (id_deputado_frente);