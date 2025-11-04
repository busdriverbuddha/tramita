-- ### 3.1.13 Tramitações

%%sql
ALTER TABLE tramitacoes_camara
    ALTER COLUMN id_tramitacao TYPE BIGINT;

ALTER TABLE tramitacoes_camara
    ADD CONSTRAINT pk_tramitacoes
    PRIMARY KEY (id_tramitacao);