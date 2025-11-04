-- ### 2.1.8 Proposições

%%sql
CREATE OR REPLACE VIEW bronze_camara_proposicoes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/proposicoes/details/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'proposicoes';

SELECT COUNT(*) AS n FROM bronze_camara_proposicoes;
