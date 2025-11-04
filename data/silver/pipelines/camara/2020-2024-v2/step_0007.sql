-- ### 2.1.3 Eventos

%%sql
CREATE OR REPLACE VIEW bronze_camara_eventos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/eventos/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'eventos';

SELECT COUNT(*) AS n FROM bronze_camara_eventos;