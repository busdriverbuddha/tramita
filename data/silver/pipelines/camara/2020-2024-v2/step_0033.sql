-- ### 2.3.3 Deputados e histórico

%%sql
CREATE OR REPLACE VIEW bronze_camara_deputados_historico AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/deputados/historico/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'deputados/historico';

SELECT COUNT(*) AS n FROM bronze_camara_deputados_historico;