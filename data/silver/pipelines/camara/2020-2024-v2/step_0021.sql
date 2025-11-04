-- ## 2.2 Modelos factuais
-- ### 2.2.1 Autores

%%sql
CREATE OR REPLACE VIEW bronze_camara_autores AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/autores/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'autores';

SELECT COUNT(*) AS n FROM bronze_camara_autores;