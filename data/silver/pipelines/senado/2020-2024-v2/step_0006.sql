-- ### 2.1.2 Colegiado

%%sql
CREATE OR REPLACE VIEW bronze_senado_colegiado AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/colegiado/details/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'colegiado';

SELECT COUNT(*) AS n FROM bronze_senado_colegiado;