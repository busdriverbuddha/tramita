-- ### 2.3.9 Partidos e líderes

%%sql
CREATE OR REPLACE VIEW bronze_partidos_lideres AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/partidos/lideres/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'partidos/lideres';

SELECT COUNT(*) AS n FROM bronze_partidos_lideres;
