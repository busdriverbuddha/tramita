-- ### 2.1.4 Frentes

%%sql
CREATE OR REPLACE VIEW bronze_camara_frentes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/frentes/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'frentes';

SELECT COUNT(*) AS n FROM bronze_camara_frentes;