-- ### 2.1.2 Deputados

%%sql
CREATE OR REPLACE VIEW bronze_camara_deputados AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/deputados/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'deputados';

SELECT COUNT(*) AS n FROM bronze_camara_deputados;