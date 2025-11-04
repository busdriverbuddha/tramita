-- ### 2.1.9 Temas

%%sql
CREATE OR REPLACE VIEW bronze_camara_temas AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/temas/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'temas';

SELECT COUNT(*) AS n FROM bronze_camara_temas;