-- ### 2.2.3 Votações e votos

%%sql
CREATE OR REPLACE VIEW bronze_senado_votacoes AS
SELECT * FROM parquet_scan("data/bronze/snapshots/bronze-2020-2024-v2/senado/votacoes/year=*/part-*.parquet")
WHERE source = 'senado' AND entity = 'votacoes';

SELECT COUNT(*) AS n FROM bronze_senado_votacoes;