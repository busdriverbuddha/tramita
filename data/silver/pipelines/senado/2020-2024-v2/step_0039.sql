-- # 3. Regularização
-- 
-- # 3.1. Normalização de PKs
-- ### 3.1.1. Bloco

%%sql
ALTER TABLE bloco_senado
    ALTER COLUMN codigo_bloco TYPE BIGINT;

ALTER TABLE bloco_senado
    ADD CONSTRAINT pk_bloco PRIMARY KEY (codigo_bloco);