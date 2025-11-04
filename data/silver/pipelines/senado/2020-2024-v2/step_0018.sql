-- ### 2.2.2 Relatorias

%%sql
CREATE OR REPLACE VIEW bronze_senado_relatorias AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/relatorias/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'relatorias';

SELECT COUNT(*) AS n FROM bronze_senado_relatorias;