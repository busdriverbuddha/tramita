-- # 3. Regularização
-- 
-- ## 3.1. Normalização de PKs
-- 
-- Aqui vamos determinar as chaves primárias (PK) de cada tabela, deduplicando onde necessário.
-- ### 3.1.2 Blocos

%%sql
CREATE TABLE blocos_camara_dedup AS
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY id_bloco ORDER BY year_snapshot DESC) AS rn
    FROM blocos_camara
)
WHERE rn = 1;

DROP TABLE blocos_camara;
ALTER TABLE blocos_camara_dedup RENAME TO blocos_camara;