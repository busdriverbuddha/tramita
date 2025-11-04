-- ### 2.2.2 Orientações

%%sql
CREATE OR REPLACE VIEW bronze_camara_orientacoes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/orientacoes/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'orientacoes';

SELECT COUNT(*) AS n FROM bronze_camara_orientacoes;