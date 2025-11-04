-- ### 3.1.9 Proposições

%%sql
ALTER TABLE proposicoes_camara
    ALTER COLUMN id_proposicao TYPE BIGINT;

ALTER TABLE proposicoes_camara
    ADD CONSTRAINT pk_proposicoes PRIMARY KEY (id_proposicao);