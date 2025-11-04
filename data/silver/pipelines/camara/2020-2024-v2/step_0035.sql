-- ### 2.3.4 Deputados e órgãos

%%sql
CREATE OR REPLACE VIEW bronze_camara_deputados_orgaos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/deputados/orgaos/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'deputados/orgaos';

SELECT COUNT(*) AS n FROM bronze_camara_deputados_orgaos;