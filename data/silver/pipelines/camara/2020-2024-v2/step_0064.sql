-- ### 3.1.11 Autores

%%sql
ALTER TABLE autores_camara
    ALTER COLUMN id_proposicao TYPE BIGINT;

ALTER TABLE autores_camara
    ALTER COLUMN ordem_assinatura TYPE INTEGER;