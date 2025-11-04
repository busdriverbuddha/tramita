-- # 2. Extração inicial
-- 
-- ## 2.1. Modelos dimensionais
-- ### 2.1.1 Bloco

%%sql
CREATE OR REPLACE VIEW bronze_senado_bloco AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/bloco/details/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'bloco';

SELECT COUNT(*) AS n FROM bronze_senado_bloco;
