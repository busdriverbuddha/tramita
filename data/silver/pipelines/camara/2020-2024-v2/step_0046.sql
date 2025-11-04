-- ### 2.3.10 Partidos e membros

%%sql
CREATE OR REPLACE VIEW bronze_partidos_membros AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/partidos/membros/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'partidos/membros';

SELECT COUNT(*) AS n FROM bronze_partidos_membros;