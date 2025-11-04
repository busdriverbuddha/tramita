-- # 2. Extração inicial
-- 
-- ## 2.1 Modelos dimensionais
-- ### 2.1.1 Blocos

%%sql
CREATE OR REPLACE VIEW bronze_camara_blocos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/blocos/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'blocos';

SELECT COUNT(*) AS n FROM bronze_camara_blocos;
