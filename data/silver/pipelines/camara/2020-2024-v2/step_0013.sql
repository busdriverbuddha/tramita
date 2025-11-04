-- ### 2.1.6 Órgaos

%%sql
CREATE OR REPLACE VIEW bronze_camara_orgaos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/orgaos/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'orgaos';

SELECT COUNT(*) AS n FROM bronze_camara_orgaos;
