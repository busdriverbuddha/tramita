-- ### 2.3.5 Eventos e órgaos

%%sql
CREATE OR REPLACE VIEW bronze_camara_eventos_orgaos AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/eventos/orgaos/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'eventos/orgaos';

SELECT COUNT(*) AS n FROM bronze_camara_eventos_orgaos;