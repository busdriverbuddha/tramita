-- ### 2.3.2 Deputados e frentes

%%sql
CREATE OR REPLACE VIEW bronze_camara_deputados_frentes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/deputados/frentes/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'deputados/frentes';

SELECT COUNT(*) AS n FROM bronze_camara_deputados_frentes;