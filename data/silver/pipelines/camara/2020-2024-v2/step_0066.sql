-- ### 3.1.12 Orientações

%%sql
ALTER TABLE orientacoes_camara
    ALTER COLUMN id_orientacao TYPE BIGINT;

ALTER TABLE orientacoes_camara
    ADD CONSTRAINT pk_orientacoes
    PRIMARY KEY (id_orientacao);