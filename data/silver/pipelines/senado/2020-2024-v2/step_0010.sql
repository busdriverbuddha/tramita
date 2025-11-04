-- ### 2.1.4 Partido

%%sql
CREATE OR REPLACE VIEW bronze_senado_partido AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/partido/details/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'partido';

SELECT COUNT(*) AS n FROM bronze_senado_partido;