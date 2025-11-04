-- ### 2.1.3 Parlamentar

%%sql
CREATE OR REPLACE VIEW bronze_senado_parlamentar AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/parlamentar/details/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'parlamentar';

SELECT COUNT(*) AS n FROM bronze_senado_parlamentar;