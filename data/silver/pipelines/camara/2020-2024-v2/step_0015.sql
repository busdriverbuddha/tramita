-- ### 2.1.7 Partidos

%%sql
CREATE OR REPLACE VIEW bronze_camara_partidos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/partidos/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'partidos';

SELECT COUNT(*) AS n FROM bronze_camara_partidos;