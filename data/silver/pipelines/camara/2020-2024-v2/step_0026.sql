-- ### 2.2.4 Votações

%%sql
CREATE OR REPLACE VIEW bronze_camara_votacoes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/camara/votacoes/year=*/part-*.parquet")
WHERE source = 'camara' AND entity = 'votacoes';

SELECT COUNT(*) AS n FROM bronze_camara_votacoes;