-- ### 2.3.6 Eventos e pautas

%%sql
CREATE OR REPLACE VIEW bronze_camara_eventos_pauta AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/eventos/pauta/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'eventos/pauta';

SELECT COUNT(*) AS n FROM bronze_camara_eventos_pauta;