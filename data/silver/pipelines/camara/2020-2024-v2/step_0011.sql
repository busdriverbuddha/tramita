-- ### 2.1.5 Legislaturas

%%sql
CREATE OR REPLACE VIEW bronze_camara_legislaturas AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/legislaturas/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'legislaturas';

SELECT COUNT(*) AS n FROM bronze_camara_legislaturas;